class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        prefix = {}
        prefix[0] = -1
        cur = res = 0
        for i,h in enumerate(hours):
            cur = cur+1 if h > 8 else cur-1
            if cur > 0:
                res = i+1
            if cur-1 in prefix:
                res = max(res, i-prefix[cur-1])
            if cur not in prefix:
                prefix[cur] = i
        return res
    
class Solution_1:
    def longestWPI(self, hours: List[int]) -> int:
        cur = res = 0
        prefix = {}
        prefix[0] = -1
        for i,h in enumerate(hours):
            cur += 1 if h > 8 else -1
            if cur > 0:
                res = max(res, i+1)
            else:
                if cur-1 in prefix:
                    res = max(res, i-prefix[cur-1])
                if cur not in prefix:
                    prefix[cur] = i
        return res
