class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def isvalid(max_sum):
            cuts = cur = 0
            for n in nums:
                cur += n
                if cur > max_sum:
                    cuts += 1
                    cur = n
            return cuts+1 <= m
        
        l, r = max(nums), sum(nums)
        while l <= r:
            mid = (l+r)//2
            if isvalid(mid):
                r = mid-1
            else:
                l = mid+1
        return l
        
