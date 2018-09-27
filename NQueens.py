import random
import numpy
import time

numIter = 0
rangeVal = int(input("Enter a range: "))
nqCandidate = list(range(rangeVal))

def Conflicts(nRange):
    numConflict = 0
    for x in range(len(nRange) - 1):
        for y in range(x + 1, len(nRange)):
            if abs(nRange[x] - nRange[y]) == abs(x - y): # finds diagonality by taking (x1-x2) and checking if it equals (y1-y2)
                numConflict += 1 # numConflict tick
    return numConflict

listTest = Conflicts(nqCandidate) # default listTest will always be [0...N-1] in numeric order

start = time.time() # used  for finding elapsed time at the end of processing

while listTest > 0:
    random.shuffle(nqCandidate) # randomize nqCandidate
    listTest = Conflicts(nqCandidate) # set listTest to new random nqCandidate 
    numIter += 1 # numIter tick

print("N = " + str(rangeVal) + " | NQ = " + str(nqCandidate)) # print correct nqCandidate & enterd N value

extraCredPrint = numpy.zeros((rangeVal, rangeVal), dtype = str) # numpy matrix of size rangVal x rangeVal, all of which are set to strings (dtype)
extraCredPrint[:] = '-' # default values in the matrix set to -

stepThru = 0

while stepThru < rangeVal:
    for x in range(len(nqCandidate)):
        for y in range(len(nqCandidate)):   
            extraCredPrint[nqCandidate[x], x] = 'Q' # replace - with Q at given coords
            stepThru += 1 # stepThru tick

print(extraCredPrint[::-1]) # printing board, [::-1] used to orient the print the correct way

end = time.time() # used  for finding elapsed time at the end of processing

print("Guessed in: " + str(numIter) + " tries") # guess number confirmation
print("Elapsed time: " + str(round(end-start, 3)) + " seconds") # elapsed time
