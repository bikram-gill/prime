'''
Find prime numbers using basic brute force.
'''

from datetime import datetime

import os

def simplePrime(    N, 
                    outputFileName, 
                    withSequenceNumber,
                    delimiter=' '):

    primeCount = 0

    outputFile = open(outputFileName, 'w')

    primes = []

    for i in range(2, N + 1):
        if not any([ i % prime == 0 for prime in primes ]):
            primes.append(i)        #number is a prime
            primeCount += 1

            #Write into a file
            if withSequenceNumber:
                outputFile.writelines(str(primeCount) + delimiter + str(i) + '\n')
            else:
                outputFile.writelines(str(i)+'\n')

    
    outputFile.close()

    return primeCount

if __name__ == '__main__':

    print('Current directory: ' + os.getcwd())

    N = int (input('Input upper bound number to find all primes (E.g. 2000000): ') )
    
    start = datetime.now()

    print('Number of prime numbers written: ', str(simplePrime(  N, './temp/primes0.txt', 
                                                                                True, ' ') ) )

    end = datetime.now()

    print( 'Start and end time: ', start.strftime("%H:%M:%S"), ' ', end.strftime("%H:%M:%S") )

    print( 'Time taken (s): ', round( (end - start).total_seconds() , 2) )
    print( 'Time taken (m): ', round( (end - start).total_seconds() / 60 , 2) )