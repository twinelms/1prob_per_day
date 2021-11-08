class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = m-1, 0
        while i >= 0 and j < n:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                j += 1
            else:
                i -= 1
        return False
