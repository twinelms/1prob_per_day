class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        s = sum(ribbons)
        if s < k: 
            return 0
        l, r = 1, min(s//k, max(ribbons))
        while l <= r:
            mid = (l+r)//2
            count = sum(x//mid for x in ribbons)
            if count < k:
                r = mid-1
            else:
                l = mid+1
        return r
