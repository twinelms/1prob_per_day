class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'T':
                    target = (i,j)
                elif grid[i][j] == 'B':
                    box = (i,j)
                elif grid[i][j] == 'S':
                    start = (i,j)
                    
        def valid(i,j):
            return 0 <= i < m and 0 <= j < n and grid[i][j] != '#'
                    
        # check if player can walk to destined point from cur position, BFS
        def can_reach(dest, cur, c_box):
            q = deque([cur])
            v = {cur}
            while q:
                i,j = cur_pos = q.popleft()
                if cur_pos == dest:
                    return True
                for next_pos in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    if valid(*next_pos) and next_pos != c_box and next_pos not in v:
                        q.append(next_pos)
                        v.add(next_pos)
            return False
            
        queue = deque([(0,box,start)])
        visited = {(box,start)}
        while queue:    # move box, BFS
            pushes, cur_box, cur_per = queue.popleft()
            if cur_box == target:
                return pushes
            bx,by = cur_box
            pair = (((bx-1,by),(bx+1,by)),
                    ((bx+1,by),(bx-1,by)),
                    ((bx,by-1),(bx,by+1)),
                    ((bx,by+1),(bx,by-1))
            )
            for new_box,new_per in pair:
                if valid(*new_box) and valid(*new_per) and (new_box, cur_box) not in visited:
                    if can_reach(new_per,cur_per,cur_box):
                        visited.add((new_box,cur_box))
                        queue.append((pushes+1,new_box,cur_box))
        return -1
            
