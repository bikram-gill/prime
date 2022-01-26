'''
Utility functions for prime project.
'''
import datetime

'''
Write list contents into a file, one list item per line.
'''
def printListToFile(fileName, inputList, appendFlag=False, consolePrint=True):
    file = None

    if appendFlag:
        file = open(fileName, 'a')
    else:
        file = open(fileName, 'w')

    for list_item in inputList:
        file.writelines(str(list_item)+'\n')

    file.close()

    if consolePrint:
        print('List contents ('+ fileName + '): ', inputList )
        print('Number of items in list ('+ fileName + '): ', str(len(inputList)) )

'''
Prints difference between start and end time, in minutes and seconds
'''
def printExecutionTime(start, end):
    print( 'Start and end time bool array: ', start.strftime("%H:%M:%S"), ' ', end.strftime("%H:%M:%S") )
    print( 'Time taken (s): ', round( (end - start).total_seconds() , 2) )
    print( 'Time taken (m): ', round( (end - start).total_seconds() / 60 , 2) )

'''
Check whether a number is a prime.
'''
def isPrime(inputNum):
    isPrimeNumber = True

    for divisor in range(2, int((inputNum / 2)) + 1):
        if inputNum % divisor == 0:
            isPrimeNumber = False
            break
    
    return isPrimeNumber

'''
Check whether a list of numbers is made up of all primes.
'''
def arePrime(numbers):
    pass  

'''
Check whether a list of numbers in a file are all primes.
'''
def containPrimes(num):
    pass





    
    