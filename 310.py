class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        nei = defaultdict(set)
        for a, b in edges:
            nei[a].add(b)
            nei[b].add(a)
        leaf = [i for i in range(n) if len(nei[i]) == 1]
        while n > 2:
            n -= len(leaf)
            new_leaf = []
            for l in leaf:
                adj = nei[l].pop()
                nei[adj].remove(l)
                if len(nei[adj]) == 1:
                    new_leaf.append(adj)
            leaf = new_leaf
        return leaf
