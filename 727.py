class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        dp = [[float('inf')]*(1+n) for _ in range(1+m)]
        # dp[i][j]: len of min window subsequence ending at s1[i] that covers s2[:j+1]
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i-1][j-1]+1 if j else 1
                else:
                    dp[i][j] = dp[i-1][j]+1
        min_len = float('inf')
        for i in range(m):
            if dp[i][n-1] < min_len:
                min_len = dp[i][n-1]
                res = s1[i+1-min_len:i+1]
        return res if min_len != float('inf') else ''
