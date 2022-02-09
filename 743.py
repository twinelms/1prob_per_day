class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        q = []
        heapq.heappush(q, (0, k))
        while q:
            t, node = heapq.heappop(q)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return t
            for v, w in graph[node]:
                heapq.heappush(q, (t+w, v))
        return -1
