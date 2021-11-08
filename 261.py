class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        parent = [i for i in range(n)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent_x, parent_y = find(x), find(y)
            if parent_x == parent_y:
                return False            
            parent[parent_x] = parent_y
            return True
        
        for a, b in edges:
            if not union(a, b):
                return False
        return True
            
