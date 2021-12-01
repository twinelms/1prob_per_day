class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat2), len(mat2[0])
        B = defaultdict(list)
        for i in range(k):
            for j in range(n):
                if mat2[i][j]:
                    B[i].append(j)
        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(k):
                if mat1[i][j]:
                    for h in B[j]:
                        res[i][h] += mat1[i][j]*mat2[j][h]
        return res
