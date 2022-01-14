class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        i = j = 0
        p_star = None
        while i < m:
            if j < n and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < n and p[j] == '*':
                p_star = j
                s_temp = i
                j += 1
            elif p_star is not None:
                j = p_star+1
                i = s_temp+1
                s_temp += 1
            else:
                return False
        for c in p[j:]:
            if c != '*':
                return False
        return True
            
