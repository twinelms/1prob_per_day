class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = []
        col = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row.append(i)
        for j in range(n):
            for i in range(m):
                if grid[i][j]:
                    col.append(j)
        dis = 0
        l, r = 0, len(row)-1
        while l <= r:
            dis += row[r]-row[l]
            l += 1
            r -= 1
        l, r = 0, len(col)-1
        while l <= r:
            dis += col[r]-col[l]
            l += 1
            r -= 1
        return dis
