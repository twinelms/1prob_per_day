class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        distinct_island = set()
        
        def track_island(direction, r, c):
            if r < 0 or c < 0 or r >= m or c >= n or not grid[r][c]:
                return
            grid[r][c] = 0
            path.append(direction)
            track_island("u", r-1, c)
            track_island("d", r+1, c)
            track_island("l", r, c-1)
            track_island("r", r, c+1)
            path.append("b")
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    path = []
                    track_island("s", i, j)
                    distinct_island.add(tuple(path))
        return len(distinct_island)
            
