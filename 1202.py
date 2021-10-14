class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = [i for i in range(len(s))]
        
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        for a,b in pairs:
            union(a,b)
        group = defaultdict(list)
        for i,c in enumerate(s):
            group[find(i)].append(c)
        for root in group:
            group[root].sort(reverse=True)
        res = []
        for i,c in enumerate(s):
            res.append(group[find(i)].pop())
        return ''.join(res)
