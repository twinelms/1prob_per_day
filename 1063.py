class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        nums.append(float('-inf'))
        stack = []
        res = 0
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] > n:
                res += i-stack.pop()
            stack.append(i)
        return res
