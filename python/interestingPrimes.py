'''
By default, primes from file ./../data/primes.txt is used as input. 

TODO: For processing primes number more than first 1M primes (upto 5M), they need to be calculated.
'''

from datetime import datetime
import os
import re

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
    
    return primesMatchingFunction (inputFileName, lambda x : all(y in x for y in list('123456789')))

'''
Find prime numbers which contain all 10 digits 0-9
'''
def primesWithAllTenDigits(   N,
                        Count,
                        inputFileName, 
                        withSequenceNumber,
                        delimiter):
    
    return primesMatchingFunction (inputFileName, all(lambda x : y in x for y in list('0123456789')))

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
                                        '^[98]{2,}$'

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
    
    pattern = r'^([1-9])\1*([1-9])\2*([1-9])\3*$'

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

    primeWithAllNineDigit = primesWithAllNineDigits(  0, 0, os.curdir + default_prime_number_file, True, ', ')
    print('Primes with all nine digits 1-9: ', primeWithAllNineDigit )
    print('Number of prime numbers, with all nine digits, in input file: ', str(len(primeWithAllNineDigit)) )
    
    palindromePrime = palindromePrimes(  0, 0, os.curdir + default_prime_number_file, True, ', ')
    print('Palindrome primes: ', palindromePrime )
    print('Number of palindrome prime numbers in input file: ', str(len(palindromePrime)) )
    
    primesWith3ConsecutiveRepeatingDigits = primesWithThreeConsecutiveRepeatingDigits(  0, 0, os.curdir + default_prime_number_file, True, ', ')
    print('Primes with 3 consecutive repeating digit: ', primesWith3ConsecutiveRepeatingDigits )
    print('Number of prime numbers in input file, with 3 consecutive repeating digit: ', str(len(primesWith3ConsecutiveRepeatingDigits)) )

    primesWithConsecutiveRepeatingDigits = primesWithConsecutiveRepeatingDigits(  0, 0, os.curdir + default_prime_number_file, True, ', ')
    print('Primes with consecutive repeating digit: ', primesWithConsecutiveRepeatingDigits )
    print('Number of prime numbers in input file, with consecutive repeating digit: ', str(len(primesWithConsecutiveRepeatingDigits)) )

    primesWithTwoRepeatingDigits = primesWithOnlyTwoRepeatingDigit(  0, 0, os.curdir + default_prime_number_file, True, ', ')
    print('Primes with two repeating digit: ', primesWithTwoRepeatingDigits )
    print('Number of prime numbers in input file, with two repeating digit: ', str(len(primesWithTwoRepeatingDigits)) )

    primesWithSingleDigit = primesWithSingleRepeatingDigit(  0, 0, os.curdir + default_prime_number_file, True, ', ')
    print('Primes with single repeating digit: ', primesWithSingleDigit )
    print('Number of prime numbers in input file, with single repeating digit: ', str(len(primesWithSingleDigit)) )

    primeWithDigitsInSequence = digitsInSequenecePrimes(  0, 0, os.curdir + default_prime_number_file, True, ', ')
    print('Primes (digits in sequence): ', primeWithDigitsInSequence )
    print('Number of prime numbers in input file, with digits in sequence: ', str(len(primeWithDigitsInSequence)) )

    primeWithDigitsInRSequence = digitsInRSequenecePrimes(  0, 0, os.curdir + default_prime_number_file, True, ', ')
    print('Primes (digits in reverse sequence): ', primeWithDigitsInRSequence )
    print('Number of prime numbers in input file, with digits in reverse sequence: ', str(len(primeWithDigitsInRSequence)) )

    end = datetime.now()
    print( 'Start and end time bool array: ', start.strftime("%H:%M:%S"), ' ', end.strftime("%H:%M:%S") )
    print( 'Time taken (s): ', round( (end - start).total_seconds() , 2) )
    print( 'Time taken (m): ', round( (end - start).total_seconds() / 60 , 2) )