class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        ret = [float('-inf')]*n
        nums.append(float('-inf'))
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                min_val = nums[stack.pop()]
                l, r = stack[-1]+1 if stack else 0, i-1
                ret[r-l] = max(ret[r-l], min_val)
            stack.append(i)
        for k in range(n-2, -1, -1):
            ret[k] = max(ret[k+1], ret[k])
        return ret
            
