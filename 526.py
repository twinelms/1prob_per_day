class Solution:
    def countArrangement(self, n: int) -> int:
        used = set()
        self.count = 0
        
        def backtrack(i):
            if i > n:
                self.count += 1
                return
            for k in range(1,n+1):
                if k not in used and (not k%i or not i%k):
                    used.add(k)
                    backtrack(i+1)
                    used.remove(k)
            
        backtrack(1)
        return self.count
