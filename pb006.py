# The sum of the squares of the first
# ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first
# ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of
# the squares of the first ten natural numbers
# and the square of the sum is
# 3025 − 385 = 2640.
# Find the difference between the sum of
# the squares of the first one hundred
# natural numbers and the square of the sum.

def sumSquare(x) :
    count = 1
    result = 0
    while count <= x :
        result += count * count
        count += 1
    return (result)

def squareSum(x) :
    count = 1
    result = 0
    while count <= x :
        result += count
        count += 1
    return (result * result)

def diffSquareSum(x) :
    return (squareSum(x) - sumSquare(x))

print(diffSquareSum(100))
