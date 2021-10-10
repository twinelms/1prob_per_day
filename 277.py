class Solution:
    def findCelebrity(self, n: int) -> int:
        i, j = 0, 1
        while j < n:
            if knows(i,j):
                candidate = j
                i = j
            else:
                candidate = i
            j += 1
                
        def validate(i):
            for k in range(n):
                if k != i: 
                    if not knows(k,i) or knows(i,k): 
                        return False
            return True
                    
                    
        if validate(candidate): 
            return candidate
        return -1
