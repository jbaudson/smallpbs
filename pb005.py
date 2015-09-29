# 2520 is the smallest number that can
# be divided by each of the numbers from
# 1 to 10 without any remainder.
# What is the smallest positive number
# that is evenly divisible by all of
# the numbers from 1 to 20?

from math import sqrt
from math import ceil

def isMinMult(x, nb) :
    count = 2
    while count <= x :
        if nb % count != 0 :
            return (False)
        count += 1
    return (True)

def minMult(x) :
    result = x
    while not isMinMult(x, result) :
        result += x
    return (result)
    
print (minMult(20))
