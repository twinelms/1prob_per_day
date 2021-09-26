class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # num1: smallest number so far
        # num2: smallest number with at least one number before it thati is smaller
        num1 = num2 = float('inf')
        for n in nums:
            if n <= num1:
                num1 = n
            elif n <= num2:
                num2 = n
            else:
                return True
        return False
