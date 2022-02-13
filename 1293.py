class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # steps, removed, pos
        m, n = len(grid), len(grid[0])
        q = deque([(0, k, 0, 0)])
        visited = {}
        visited[(0, 0)] = k
        while q:
            steps, remain, i, j = q.popleft()
            if (i, j) == (m-1, n-1):
                return steps
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] and remain and (
                        (x,y) not in visited or remain-1 > visited[(x,y)]):
                        q.append((steps+1, remain-1, x, y))
                        visited[(x,y)] = remain-1
                    elif not grid[x][y] and (
                        (x, y) not in visited or remain > visited[(x,y)]):
                        q.append((steps+1, remain, x, y))
                        visited[(x,y)] = remain
        return -1
                      
