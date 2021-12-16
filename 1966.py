class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        left = [float('-inf')]*len(nums)
        right = [float('inf')]*len(nums)
        for i in range(len(nums)-1):
            left[i+1] = max(left[i],nums[i])
        for i in range(len(nums)-1, 0, -1):
            right[i-1] = min(right[i], nums[i])
        res = 0
        for i in range(len(nums)):
            if nums[i] > left[i] and nums[i] < right[i]:
                res += 1
        return res

    
class Solution_2:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        stack = []
        max_n = float('-inf')
        for n in nums:
            while stack and stack[-1] > n:
                stack.pop()
            if n > max_n:
                stack.append(n)
                max_n = n
        return len(stack)
                
