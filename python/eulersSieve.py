'''
Find prime numbers using Eulers's Sieve.
More details: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Euler's_sieve

NOTE: This approach reduces assignments in Eratoshenes's method, but is slow due to 2 loops
Need to check possible improvements
'''

from datetime import datetime

import os

def eulersSieveBoolArray(   N, 
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

            if number == 2:
                for counter in range(number, N+1, number):
                    #Number corresponding to this index is not prime
                    primeArray[counter] = False
                    
            if number > 2:
               
                buffer = []
                
                for counter in range(number, N+1):
                    if primeArray[counter] or (buffer and counter == buffer[0]):

                        if not primeArray[counter]:
                            buffer.pop(0)
                            #print(len(buffer))

                        newNumber = counter * number

                        if newNumber < N+1 and primeArray[newNumber]:
                            primeArray[newNumber] = False
                            if (newNumber * number) < N+1:
                                buffer.append(newNumber)
                                #print(len(buffer))

        number += 1

        if number >= N:
            break
    
    outputFile.close()

    return primeCount

def eulersSieveBitArray(N):
    pass

if __name__ == '__main__':

    print('Current directory: ' + os.getcwd())

    N = int (input('Input upper bound number to find all primes (E.g. 2000000): ') )
    
    start = datetime.now()

    print('Number of prime numbers written: ', str(eulersSieveBoolArray(  N, './temp/primes2.txt', 
                                                                                True, ' ') ) )

    end = datetime.now()

    print( 'Start and end time: ', start.strftime("%H:%M:%S"), ' ', end.strftime("%H:%M:%S") )

    print( 'Time taken (s): ', round( (end - start).total_seconds() , 2) )
    print( 'Time taken (m): ', round( (end - start).total_seconds() / 60 , 2) )