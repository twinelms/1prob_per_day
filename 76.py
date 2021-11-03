class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        m, n = len(s), len(t)
        l = r = 0
        start, end = 0, -1
        while r < m:
            if count[s[r]] > 0:
                n -= 1
            count[s[r]] -= 1
            if not n:
                while l <= r and count[s[l]] != 0:
                    count[s[l]] += 1
                    l += 1
                if end < 0 or r-l < end-start:
                    start, end = l, r
            r += 1
        return s[start: end+1]
