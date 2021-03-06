class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for j in range(n):
            dp[-1][j] = j+1
        for i in range(m):
            dp[i][-1] = i+1
        for i in range(m):
            for j in range(n):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1 if word1[i] != word2[j] else dp[i-1][j-1]
        return dp[m-1][n-1]
