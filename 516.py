class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        pre = [0]*n
        for i in range(n-1, -1, -1):
            cur = [0]*n
            for j in range(i, n):
                if i == j:
                    cur[j] = 1
                else:
                    cur[j] = pre[j-1]+2 if s[i] == s[j] else max(pre[j], cur[j-1])
            pre = cur
        return pre[n-1]
