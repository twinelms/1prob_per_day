class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[-1][-1] = True
        for i in range(m, -1, -1):
            for j in range(n-1, -1, -1):
                start = i < m and p[j] in (s[i], '.')
                if j+1 < n and p[j+1] == '*':
                    dp[i][j] = (start and dp[i+1][j]) or dp[i][j+2]
                else:
                    dp[i][j] = (start and dp[i+1][j+1])
        return dp[0][0]
