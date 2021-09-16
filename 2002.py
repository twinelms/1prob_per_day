class Solution:
    def maxProduct(self, s: str) -> int:
        n, substr, res = len(s), [], 0
        for bit in range(2**n):  # bit mask
            cur = []
            for i, char in enumerate(s):
                if (bit >> i) & 1:
                    cur.append(char)
            if cur == cur[::-1]: # for each subseq, check if it is palindromic
                substr.append([bit, len(cur)])
        for bit1, l1 in substr:
            for bit2, l2 in substr:
                if bit1 & bit2 == 0:  # disjoint
                    res = max(res, l1*l2)
        return res
