class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        parent = [i for i in range(n)]
        connection = n-1
        logs.sort()
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            nonlocal connection
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
                connection -= 1
        
        for t, x, y in logs:
            union(x, y)
            if not connection:
                return t
        return -1
            
