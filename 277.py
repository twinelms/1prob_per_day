# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        i, j = 0, 1
        memo = {}
        
        def findmemo(a, b):
            if (a,b) not in memo:
                memo[(a,b)] = knows(a,b)
            return memo[(a,b)]
        
        while j < n:
            if findmemo(i, j):
                i = j
            j += 1
            
        for p in range(n):
            if p != i:
                if not findmemo(p, i) or findmemo(i, p):
                    return -1
        return i
