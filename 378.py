class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        s, l, n = matrix[0][0], matrix[-1][-1], len(matrix)
        
        def count(tgt):
            i, j = n-1, 0
            count = 0
            while i >= 0 and j < n:
                if matrix[i][j] > tgt:
                    i -= 1
                else:
                    count += i+1
                    j += 1
            return count
        
        while s <= l:
            med = (s+l)//2
            ste = count(med)  # num of ele ( ele <= med )
            if ste < k:
                s = med+1
            else:
                l = med-1
        return s
