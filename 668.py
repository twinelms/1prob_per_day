class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def find(num):
            ret = 0
            for i in range(1, m+1):
                ret += min(num//i, n)
            return ret
        
        l, r = 1, m*n
        while l < r:
            mid = (l+r)//2
            count = find(mid) # number of integers which are <= mid
            if count < k:
                l = mid+1
            else:
                r = mid
        return l
