# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13, we can see that
# the 6th prime is 13.
# What is the 10 001st prime number?

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

def primeNumber(x) :
    count = 0
    nb = 0
    prime = 0
    while nb < x :
        if isPrime(count) :
            prime = count
            nb += 1
        count += 1
    return (prime)

print(primeNumber(10001))
