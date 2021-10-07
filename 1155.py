class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0]*(target+1) for _ in range(d)]
        for i in range(1, min(f+1,target+1)):
            dp[0][i] = 1
        for i in range(1, d):
            for j in range(target+1):
                for k in range(1, f+1):
                    if j-k >= 0: dp[i][j] = (dp[i]+dp[i-1][j-k])%(10**9+7)
        return dp[-1][target]
