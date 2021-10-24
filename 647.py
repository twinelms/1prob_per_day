class Solution:
    def countSubstrings(self, s: str) -> int:
        # 2n-1 possible centers for expanding a palindromic string
        res = 0
        
        def count(i,j):
            ret = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                ret += 1
                i -= 1
                j += 1
            return ret
            
        
        for i in range(len(s)):
            res += count(i,i)
            res += count(i,i+1)
        return res
                
