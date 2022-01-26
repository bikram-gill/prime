'''
By default, primes from file ./../data/primes.txt is used as input. 

TODO: For processing primes number more than first 1M primes (upto 5M), they need to be calculated.
'''

from datetime import datetime
import os
import re

import primeUtil

default_prime_number_file = '\prime\data\primes.txt'

'''
Find prime numbers which are also palindrome numbers
'''
def palindromePrimes(   N,
                        Count,
                        inputFileName, 
                        withSequenceNumber,
                        delimiter):
    
    return primesMatchingFunction (inputFileName, lambda x : x == x[::-1])

'''
Find prime numbers which contain all 9 digits 1-9.
Note: Input file needs very large prime numbers.
'''
def primesWithAllNineDigits(   N,
                        Count,
                        inputFileName, 
                        withSequenceNumber,
                        delimiter):
    
    #TODO need to find a faster alternative
    return primesMatchingFunction (inputFileName, lambda prime : all(digit in prime for digit in list('123456789')))

'''
Find prime numbers which contain all 10 digits 0-9
'''
def primesWithAllTenDigits(   N,
                        Count,
                        inputFileName, 
                        withSequenceNumber,
                        delimiter):
    
    return primesMatchingFunction (inputFileName, all(lambda prime : digit in prime for digit in list('0123456789')))

'''
Find prime numbers which have digits [1-9] in ascending sequence, e.g. 13, 23, but not 31
'''
def digitsInSequenecePrimes(   N,
                        Count,
                        inputFileName, 
                        withSequenceNumber,
                        delimiter):
    
    pattern = r'^1*?2*?3*?4*?5*?6*?7*?8*?9*?$'

    return primesMatchingRegex( inputFileName, pattern)

'''
Find prime numbers which have digits [1-9] in descending sequence, e.g. 31, 97, but not 23
'''
def digitsInRSequenecePrimes(   N,
                        Count,
                        inputFileName, 
                        withSequenceNumber,
                        delimiter):
    
    pattern = r'^9*?8*?7*?6*?5*?4*?3*?2*?1*?$'

    return primesMatchingRegex( inputFileName, pattern)

    
'''
Find prime numbers with single repeating digit, e.g. 11

Actually, till first 26M primes, 11 is the only such number.
'''
def primesWithSingleRepeatingDigit( N,
                                    Count,
                                    inputFileName, 
                                    withSequenceNumber,
                                    delimiter):
    
    pattern = r'^11+$|^22+$|^33+$|^44+$|^55+$|^66+$|^77+$|^88+$|^99+$'

    return primesMatchingRegex( inputFileName, pattern)

'''
Find prime numbers with single repeating digit, e.g. 11

Only the specific numbers are computed and tested for prime, instead of testing all primes.

This function can be very slow, only partially tested.
'''
def primesWithSingleRepeatingDigit2( N,
                                    Count,
                                    withSequenceNumber,
                                    delimiter):
    primes = []

    #Repeating even digits cannot create a prime, as they are divisible by 2
    #Repeating digit 5 will always be divisible by 5
    #Repeating digit 3 or 9 will always be divisible by 3
    #Repeating digit 7 is always be divisible by 7
    #So we only have digit 1 to test
    
    number = '1'
    digit = '1'

    #Random number, 300, approx upper limit based on testing on a normal 64 bit system
    #But limit 50 can also take a lot of time to execute
    for _ in range(1,50):
        number += digit
        isPrime = True
        length = len(number)
        
        #Ignore numbers divisible by 3 (divisibility rule) 
        if length % 3 == 0:
            continue

        int1 = int(number)

        #Check divisibility by odd numbers
        for divisor in range(3, int(int1 / 2) + 1, 2):
            if int1 % divisor == 0:
                isPrime = False
                break
        
        if isPrime:
            primes.append(number)
            print('Prime: ' + str(number))

    return primes
    
'''
Find prime numbers made up of only 2 digits, each occuring at least 1 time.
E.g. 11111117, 18888811, 19991911, but not 112878211 which has 1, 2, 8, and 7
'''
def primesWithOnlyTwoRepeatingDigit( N,
                                    Count,
                                    inputFileName, 
                                    withSequenceNumber,
                                    delimiter):
    
    pattern = r'^[12]{2,}$|^[13]{2,}$|^[14]{2,}$|^[15]{2,}$|^[16]{2,}$|^[17]{2,}$|^[18]{2,}$|^[19]{2,}$|' + \
                '^[23]{2,}$|^[24]{2,}$|^[25]{2,}$|^[26]{2,}$|^[27]{2,}$|^[28]{2,}$|^[29]{2,}$|' + \
                    '^[34]{2,}$|^[35]{2,}$|^[36]{2,}$|^[37]{2,}$|^[38]{2,}$|^[39]{2,}$|' + \
                        '^[45]{2,}$|^[46]{2,}$|^[47]{2,}$|^[48]{2,}$|^[49]{2,}$|' + \
                            '^[56]{2,}$|^[57]{2,}$|^[58]{2,}$|^[59]{2,}$|' + \
                                '^[67]{2,}$|^[68]{2,}$|^[69]{2,}$|' + \
                                    '^[78]{2,}$|^[79]{2,}$|' + \
                                        '^[98]{2,}$|' + \
                                            '^[01]{2,}$|^[07]{2,}$'

    return primesMatchingRegex( inputFileName, pattern)

'''
Find prime numbers made up of only 2 digits, each occuring at least 1 times with consecutive repetition.
E.g. 11111777, 6677777, with form mmmmmnnnnnn (m and n could be of variable lengths), 
but not 11113367 which has form llllmmno
'''
def primesWithConsecutiveRepeatingDigits( N,
                                    Count,
                                    inputFileName, 
                                    withSequenceNumber,
                                    delimiter):
    
    pattern = r'^([1-9])\1*([1-9])\2*$'

    return primesMatchingRegex( inputFileName, pattern)

'''
Find prime numbers made up of only 3 digits, each occuring at least 1 times with consecutive repetition.
E.g. 4446677, 3388999, with form mmmnnnnoo (m, n and o could be of variable lengths), 
but not 11113367 which has form llllmmno
'''
def primesWithThreeConsecutiveRepeatingDigits( N,
                                    Count,
                                    inputFileName, 
                                    withSequenceNumber,
                                    delimiter):
    
    pattern = r'^([1-9])\1*([0-9])\2*([1-9])\3*$'

    return primesMatchingRegex( inputFileName, pattern)

'''
Find prime numbers with alternate repeating digits.
E.g.  with form nonononon (n and o alternately repeating).
'''
def primesWithAlternateRepeatingDigits( N,
                                    Count,
                                    inputFileName, 
                                    withSequenceNumber,
                                    delimiter):
    
    pattern = r'^([1-9])([0-9])(\1\2)*\1?$'

    return primesMatchingRegex( inputFileName, pattern)

'''
Find prime numbers matching input regex
'''
def primesMatchingRegex(    inputFileName, 
                            pattern):
    
    input_file = open(inputFileName, 'r')
    
    primes = []

    while True:
        line = input_file.readline().strip()

        if not line:
            break

        if re.search(pattern, line):
            primes.append(int(line))

    input_file.close()

    return primes


'''
Find prime numbers matching input function, which returns a bool.
All primes for which function returns true are returned
'''
def primesMatchingFunction( inputFileName, 
                            function):
    
    input_file = open(inputFileName, 'r')
    
    primes = []

    while True:
        line = input_file.readline().strip()

        if not line:
            break

        if function(line):
            primes.append(int(line))

    input_file.close()

    return primes

if __name__ == '__main__':

    print('Current directory: ' + os.getcwd())

    # option = input('Input upper bound (1) or prime number count (2) to find palindrome primes: ')
    
    # Num = 0
    # Count = 0
    
    # if option == '1':
    #     Num = int (input('Input upper bound number to find all primes (E.g. 1000000): ') )
    # elif option == '2':
    #     Count = int (input('Input number of primes to calculate (E.g. 100): ') )
    # else:
    #     print('Select 1 or 2')
    #     exit()
    
    # withSequenceNumber = input('Print sequence number of prime (Y/N): ')
    
    # if withSequenceNumber == 'Y' or  withSequenceNumber == 'y':
    #     withSequenceNumber = True
    # else:
    #     withSequenceNumber = False
    
    start = datetime.now()
    
    #primes = palindromePrimes(  Num, Count, os.curdir + '\prime\data\million-primes.txt', withSequenceNumber, ', ')

    primesWithSingleDigit1 = primesWithSingleRepeatingDigit2(  0, 0, True, ', ')
    primeUtil.printListToFile('primes-with-single-repeating-digits1.txt', primesWithSingleDigit1)

    primesWithSingleDigit2 = primesWithSingleRepeatingDigit(  0, 0, os.curdir + default_prime_number_file, True, ', ')
    primeUtil.printListToFile('primes-with-single-repeating-digits2.txt', primesWithSingleDigit2)

    palindromePrime = palindromePrimes(  0, 0, os.curdir + default_prime_number_file, True, ', ')
    primeUtil.printListToFile('primes-palindrome.txt', palindromePrime)

    primesWith3ConsecutiveRepeatingDigits = primesWithThreeConsecutiveRepeatingDigits(  0, 0, os.curdir + default_prime_number_file, True, ', ')
    primeUtil.printListToFile('primes-3-consecutive-repeating-digits.txt', primesWith3ConsecutiveRepeatingDigits)

    primesWithConsecutiveRepeatingDigits = primesWithConsecutiveRepeatingDigits(  0, 0, os.curdir + default_prime_number_file, True, ', ')
    primeUtil.printListToFile('primes-with-consecutive-repeating-digits.txt', primesWithConsecutiveRepeatingDigits)

    primesWithTwoRepeatingDigits = primesWithOnlyTwoRepeatingDigit(  0, 0, os.curdir + default_prime_number_file, True, ', ')
    primeUtil.printListToFile('primes-with-consecutive-2-repeating-digits.txt', primesWithTwoRepeatingDigits)

    primeWithDigitsInSequence = digitsInSequenecePrimes(  0, 0, os.curdir + default_prime_number_file, True, ', ')
    primeUtil.printListToFile('primes-digits-in-ascending-sequence.txt', primeWithDigitsInSequence)

    primeWithDigitsInRSequence = digitsInRSequenecePrimes(  0, 0, os.curdir + default_prime_number_file, True, ', ')
    primeUtil.printListToFile('primes-digits-in-descending-sequence.txt', primeWithDigitsInRSequence)

    primeWithAllNineDigit = primesWithAllNineDigits(  0, 0, os.curdir + default_prime_number_file, True, ', ')
    primeUtil.printListToFile('primes-with-all-nine-digits.txt', primeWithAllNineDigit)

    primesWithAlternateRepeatingDigit = primesWithAlternateRepeatingDigits(  0, 0, os.curdir + default_prime_number_file, True, ', ')
    primeUtil.printListToFile('primes-with-alternate-repeating-digits.txt', primesWithAlternateRepeatingDigit)

    primeUtil.printExecutionTime(start, datetime.now())
    