class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target = sum(nums)//2
        dp = [False]*(target+1)
        dp[0] = True
        for n in nums:
            for i in range(target, -1, -1):
                if dp[i] and i+n <= target:
                    dp[i+n] = True
        return dp[target]
