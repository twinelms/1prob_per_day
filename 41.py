class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        l = len(nums)
        for i in range(l):
            if nums[i] <= 0 or nums[i] > l:
                nums[i] = 1
        for n in nums:
            idx = abs(n)-1
            nums[idx] = -abs(nums[idx])
        for i, n in enumerate(nums):
            if n > 0:
                return i+1
        return l+1
            
