class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1]*len(nums)
        for _ in range(2):
            for i, n in enumerate(nums):
                while stack and n > nums[stack[-1]]:
                    idx = stack.pop()
                    ans[idx] = n
                stack.append(i)
        return ans
