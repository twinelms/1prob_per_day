class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = []
        cur = n*n
        while cur:
            sm, lg = cur-len(mat)+1, cur
            row = [x for x in range(sm, lg+1)]
            mat = [row]+list(zip(*mat[::-1]))
            cur = sm-1
        return mat

      
    def generateMatrix2(self, n: int) -> List[List[int]]:
        mat = [[0]*n for _ in range(n)]
        i,j,cur,di,dj = 0,0,1,0,1
        while cur <= n*n:
            mat[i][j] = cur
            cur += 1
            if i+di < 0 or i+di >=n or j+dj < 0 or j+dj >= n or mat[i+di][j+dj]:
                di, dj = dj, -di  # important trick 0,1;1,0;0,-1;-1,0
            i += di
            j += dj
        return mat
