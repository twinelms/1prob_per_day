class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        bus = defaultdict(set)
        for i,route in enumerate(routes):
            for stop in route:
                bus[stop].add(i)
        res = 0
        q = deque([(1, r) for r in bus[source]])
        visited = set()
        while q:
            buses, cur_route = q.popleft()
            if cur_route in visited:
                continue
            visited.add(cur_route)
            for stop in routes[cur_route]:
                if stop == target:
                    return buses
                for route in bus[stop]:
                    if route != cur_route: 
                        q.append((buses+1, route))
        return -1
