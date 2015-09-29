# A palindromic number reads the same
# both ways. The largest palindrome made
# from the product of two 2-digit numbers
# is 9009 = 91 × 99.
# Find the largest palindrome made from
# the product of two 3-digit numbers.

def isPalin(x) :
    s = str(x)
    count = 0
    while count < int(len(s) / 2) :
        if s[count] != s[len(s) - 1 - count] :
            return (False)
        count += 1
    return (True)

def maxPalin(x, y, number) :
    count = x
    palinMax = 0
    z = 10 ^ (number - 1)
    while count > z:
        if isPalin(count * y) and (count * y > palinMax) :
            palinMax = count * y
            y -= 1
            count = x + 1
        count -= 1
        if (y > z) and (count == z) :
            y -= 1
            count = x
    return (palinMax)
    
print(maxPalin(999, 999, 3))
