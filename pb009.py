# A Pythagorean triplet is a set of
# three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean
# triplet for which a + b + c = 1000.
# Find the product abc.

from math import sqrt

def pythagorean(x) :
    a = 1
    b = 1
    while b <= x :
        while a < b :
            if (a + b + sqrt(a*a + b*b) == x) :
                print(a,b, sqrt(a*a+b*b))
                return (a * b * sqrt(a*a + b*b))
            a += 1
        b += 1
        a = 1
    return (-1)

print(pythagorean(1000))

#def pyth(x):
#   for a in range( x / 2):
#       for b in range(x / 2):
#           c = x - a - b
#               if a * a + b * b == c * c:
#                   return a * b * c
# print pyth(1000)
