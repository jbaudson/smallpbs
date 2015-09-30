# The following iterative sequence is defined for
# the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13,
# we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at
# 13 and finishing at 1) contains 10 terms. Although
# it has not been proved yet (Collatz Problem), it
# is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces
# the longest chain?

def maxCollatzSeq(x) :
    maxChain = 0
    i = 1
    if x == 1 :
        return (0)
    while i < x :
        j = i
        tmp = 1
        while j > 1 :
            if j % 2 :
                j = 3 * j + 1
            else :
                j /= 2
            tmp += 1
        if tmp > maxChain :
            maxChain = tmp
            rank = i
        #print(maxChain)
        i += 1
    return (maxChain, rank)
    
print(maxCollatzSeq(1000000))
