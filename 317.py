class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:   
        m,n = len(grid),len(grid[0])
        dis = [[0]*n for _ in range(m)]
        cur = 0
        
        def bfs(i,j,cur):
            queue = deque([(i,j,0)])
            while queue:
                i,j,d = queue.popleft()
                for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == cur:
                        grid[x][y] -= 1
                        dis[x][y] += d+1
                        queue.append((x,y,d+1))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i,j,cur)
                    cur -= 1
        res = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == cur:
                    res = min(res,dis[i][j])
        return res if res != float('inf') else -1
