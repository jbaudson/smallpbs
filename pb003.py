# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor
# of the number 600851475143 ?

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

x = 600851475143
count = 2
while count <= ceil(sqrt(x)) :
    if (isPrime(count)) and (x % count == 0) :
        x /= count
        count -= 1
    count += 1
print(int(x))
