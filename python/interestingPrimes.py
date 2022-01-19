'''
Primes from file ./../data/million-primes.txt is used as input. 

TODO: For processing primes number more than first 1M primes (upto 5M), they need to be calculated.
'''

from datetime import datetime
import os
import re

'''
Find prime numbers which are also palindrome numbers
'''
def palindromePrimes(   N,
                        Count,
                        inputFileName, 
                        withSequenceNumber,
                        delimiter):
    
    input_file = open(inputFileName, 'r')
    
    palindromes = []

    while True:
        line = input_file.readline().strip()

        if not line:
            break

        if line == line[::-1]:
            palindromes.append(int(line))

    input_file.close()

    return palindromes

'''
Find prime numbers which have digits [1-9] in sequence, e.g. 13, 23, but not 31
'''
def digitsInSequenecePrimes(   N,
                        Count,
                        inputFileName, 
                        withSequenceNumber,
                        delimiter):
    
    input_file = open(inputFileName, 'r')
    
    primeWithDigitsInSequence = []

    pattern = r'^1*?2*?3*?4*?5*?6*?7*?8*?9*?$'

    while True:
        line = input_file.readline().strip()

        if not line:
            break

        if re.search(pattern, line):
            primeWithDigitsInSequence.append(int(line))

    input_file.close()

    return primeWithDigitsInSequence

'''
Find prime numbers which have digits [1-9] in reverse sequence, e.g. 31, 97, but not 23
'''
def digitsInRSequenecePrimes(   N,
                        Count,
                        inputFileName, 
                        withSequenceNumber,
                        delimiter):
    
    input_file = open(inputFileName, 'r')
    
    primeWithDigitsInRSequence = []

    pattern = r'^9*?8*?7*?6*?5*?4*?3*?2*?1*?$'

    while True:
        line = input_file.readline().strip()

        if not line:
            break

        if re.search(pattern, line):
            primeWithDigitsInRSequence.append(int(line))

    input_file.close()

    return primeWithDigitsInRSequence

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
    primes = palindromePrimes(  0, 0, os.curdir + '\prime\data\million-primes.txt', True, ', ')
    print('Palindrome primes: ', primes )
    print('Number of palindrome prime numbers below 1M: ', str(len(primes)) )
    
    primeWithDigitsInSequence = digitsInSequenecePrimes(  0, 0, os.curdir + '\prime\data\million-primes.txt', True, ', ')
    print('Primes (digits in sequence): ', primeWithDigitsInSequence )
    print('Number of prime numbers below 1M, with digits in sequence: ', str(len(primeWithDigitsInSequence)) )

    primeWithDigitsInRSequence = digitsInRSequenecePrimes(  0, 0, os.curdir + '\prime\data\million-primes.txt', True, ', ')
    print('Primes (digits in reverse sequence): ', primeWithDigitsInRSequence )
    print('Number of prime numbers below 1M, with digits in reverse sequence: ', str(len(primeWithDigitsInRSequence)) )

    end = datetime.now()
    print( 'Start and end time bool array: ', start.strftime("%H:%M:%S"), ' ', end.strftime("%H:%M:%S") )
    print( 'Time taken (s): ', round( (end - start).total_seconds() , 2) )
    print( 'Time taken (m): ', round( (end - start).total_seconds() / 60 , 2) )