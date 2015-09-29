# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from math import sqrt
from math import ceil

def isPrime(x) :
    if x < 2 :
        return (False)
    count = 2
    while count <= ceil(sqrt(x)) :
        if x % count == 0 and x != count:
            return (False)
        count += 1
    return (True)

def sumPrime(x) :
    count = 3
    result = 2
    if x < 2 :
        return (0)
    if x == 2 :
        return (2)
    if x == 3 or x == 4:
        return (5)
    while count < x :
        if isPrime(count) :
            result += count
        count += 2
    return (result)

print(sumPrime(2000000))
