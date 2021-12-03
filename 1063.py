class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        first_small = [len(nums)]*len(nums)
        stack = []
        for i, n in enumerate(nums):
            while stack and stack[-1][1] > n:
                first_small[stack.pop()[0]] = i
            stack.append((i,n))
        res = 0
        for start, end in enumerate(first_small):
            res += end-start
        return res
