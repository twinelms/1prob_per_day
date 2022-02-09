class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for a, b, p in flights:
            graph[a].append((b, p))
        q = [(0, -1, src)]
        visited = {}
        while q:
            p, stops, cur = heapq.heappop(q)
            if cur == dst:
                return p
            if cur in visited and stops > visited[cur]:
                continue
            visited[cur] = stops
            if stops < k:
                for b, p1 in graph[cur]:
                    heapq.heappush(q, (p+p1, stops+1, b))
        return -1
