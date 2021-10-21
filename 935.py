class Solution:
    def knightDialer(self, n: int) -> int:
        ref = {
            1: (8,6),
            2: (7,9),
            3: (4,8),
            4: (3,9,0),
            5: (), 
            6: (1,7,0),
            7: (2,6),
            8: (1,3),
            9: (2,4),
            0: (4,6)    
        }
        
        if n == 1:
            return 10
        pre = [1]*5 + [0] +[1]*4
        for i in range(2, n+1):
            cur = [0]*10
            for i,f in enumerate(pre):
                for digit in ref[i]: 
                    cur[digit] = (cur[digit]+f)%(10**9+7)
            pre = cur
        return sum(pre)%(10**9+7)
