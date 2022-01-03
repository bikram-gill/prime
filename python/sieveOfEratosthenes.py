'''
Find prime numbers using Sieve Of Eratosthenes.
'''

from datetime import datetime

import os

def sieveOfEratosthenesBoolArray( N, 
                                outputFileName, 
                                withSequenceNumber,
                                delimiter=' '):
    
    #initialize prime number array, number corresponding to index is a prime if value is True (except first 2)
    primeArray = [True for _ in range(N+1)] 
    
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

            for counter in range(number * 2, N+1, number):
                #Number corresponding to this index is not prime
                if primeArray[counter]:
                    primeArray[counter] = False

        number += 1

        if number >= N:
            break
    
    outputFile.close()

    return primeCount

def sieveOfEratosthenesBitArray(N):
    pass

if __name__ == '__main__':

    print('Current directory: ' + os.getcwd())

    N = int (input('Input upper bound number to find all primes (E.g. 2000000): ') )
    
    start = datetime.now()

    print('Number of prime numbers written: ', str(sieveOfEratosthenesBoolArray(  N, './temp/primes.txt', 
                                                                                True, ' ') ) )

    end = datetime.now()

    print( 'Start and end time: ', start.strftime("%H:%M:%S"), ' ', end.strftime("%H:%M:%S") )

    print( 'Time taken (s): ', round( (end - start).total_seconds() , 2) )
    print( 'Time taken (m): ', round( (end - start).total_seconds() / 60 , 2) )