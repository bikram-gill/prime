'''
Find prime numbers using Sieve Of Eratosthenes.
More details: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
'''

from datetime import datetime

#to install --> pip install bitarray
from bitarray import bitarray

import os
import sys

def sieveOfEratosthenesBoolArray( N,
                                Count,
                                outputFileName, 
                                withSequenceNumber,
                                delimiter):
    
    if N == 0:
        N = 100000000 #Random upper limit to allow calculation of around 5M primes
    
    #initialize prime number array, number corresponding to index is a prime if value is True (except first 2)
    primeArray = [True for _ in range(N+1)]

    print('Size of bool array: ' + str(sys.getsizeof(primeArray)))

    number = 2 #start with first prime
    
    primeCount = 0

    outputFile = open(outputFileName, 'w')

    while True:    
        #If current number is a prime, mark its multiples out of the primeArray
        if primeArray[number]:
            
            primeCount += 1
            
            #Write into a file
            if withSequenceNumber:
                outputFile.writelines(str(primeCount) + delimiter + str(number) + '\n')
            else:
                outputFile.writelines(str(number)+'\n')

            #If this is count based calculation, break when needed primes are calculated
            if Count != 0 and Count <= primeCount:
                break

            for counter in range(number * 2, N+1, number):
                #Number corresponding to this index is not prime
                if primeArray[counter]:
                    primeArray[counter] = False

        number += 1

        if number >= N:
            break
    
    outputFile.close()

    return primeCount

def sieveOfEratosthenesBitArray(    N, 
                                    Count,
                                    outputFileName, 
                                    withSequenceNumber,
                                    delimiter):

    if N == 0:
        N = 100000000 #Random upper limit to allow calculation of around 5M primes

    #initialize prime number array, number corresponding to index is a prime if value is 1 (except first 2)
    primeArray = bitarray(N+1)
    primeArray.setall(1)

    print('Size of bit array: ' + str(sys.getsizeof(primeArray)))

    number = 2 #start with first prime
    
    primeCount = 0

    outputFile = open(outputFileName, 'w')

    while True:    
        #If current number is a prime, mark its multiples out of the primeArray
        if primeArray[number] == 1:
            
            primeCount += 1
            
            #Write into a file
            if withSequenceNumber:
                outputFile.writelines(str(primeCount) + delimiter + str(number) + '\n')
            else:
                outputFile.writelines(str(number)+'\n')

            #If this is count based calculation, break when needed primes are calculated
            if Count != 0 and Count <= primeCount:
                break

            for counter in range(number * 2, N+1, number):
                #Number corresponding to this index is not prime
                if primeArray[counter] == 1:
                    primeArray[counter] = 0

        number += 1

        if number >= N:
            break
    
    outputFile.close()

    return primeCount


if __name__ == '__main__':

    print('Current directory: ' + os.getcwd())

    option = input('Input upper bound (1) or prime number count (2) to calculate: ')
    Num = 0
    Count = 0
    if option == '1':
        Num = int (input('Input upper bound number to find all primes (E.g. 1000000): ') )
    elif option == '2':
        Count = int (input('Input number of primes to calculate (E.g. 1000000): ') )
    else:
        print('Select 1 or 2')
        exit()
    
    withSequenceNumber = input('Print sequence number of prime (Y/N): ')
    if withSequenceNumber == 'Y' or  withSequenceNumber == 'y':
        withSequenceNumber = True
    else:
        withSequenceNumber = False
    
    #NOTE: Using bitarray or boolean array does not seem to cause performance difference for calculating large number
    # of primes, as both take around 4 minutes to calculate 5M+ primes within first 100M numbers. But there is 
    # considerable difference in memory used.
    start = datetime.now()
    print('Number of prime numbers written: ', str(sieveOfEratosthenesBoolArray(  Num, Count, './temp/bitprimes1.txt', 
                                                                                  withSequenceNumber, ', ') ) )
    end = datetime.now()
    print( 'Start and end time bool array: ', start.strftime("%H:%M:%S"), ' ', end.strftime("%H:%M:%S") )
    print( 'Time taken (s): ', round( (end - start).total_seconds() , 2) )
    print( 'Time taken (m): ', round( (end - start).total_seconds() / 60 , 2) )

    start = datetime.now()
    print('Number of prime numbers written: ', str(sieveOfEratosthenesBitArray(  Num, Count, './temp/boolprimes1.txt', 
                                                                                  withSequenceNumber, ', ') ) )
    end = datetime.now()
    print( 'Start and end time bit array: ', start.strftime("%H:%M:%S"), ' ', end.strftime("%H:%M:%S") )
    print( 'Time taken (s): ', round( (end - start).total_seconds() , 2) )
    print( 'Time taken (m): ', round( (end - start).total_seconds() / 60 , 2) )

    