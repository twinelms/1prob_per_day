class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island = [0,0]
        i_id = 2
        
        def find_island(i,j,i_id):
            if i < 0 or j < 0 or i >= n or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = i_id
            return 1+find_island(i-1,j,i_id)+find_island(i+1,j,i_id)+find_island(i,j-1,i_id)+find_island(i,j+1,i_id)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island.append(find_island(i,j,i_id))
                    i_id += 1
        res = max(island)
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    nei = set(grid[a][b] for a,b in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)) if 0 <= a < n and 0 <= b < n)
                    res = max(res, 1+sum([island[idx] for idx in nei]))
        return res
