class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]: return -1
        n = len(grid)
        queue = [(0,0,1)]
        for i,j,path in queue:
            if i == n-1 and j == n-1: return path
            for x,y in ((i-1, j-1),(i-1, j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    grid[x][y] = 1
                    queue.append((x,y,path+1))
        return -1
