class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])
        fuel, ret = [], 0
        for pos, refill in stations:
            while startFuel-pos < 0:
                if not fuel:
                    return -1
                toadd = -heapq.heappop(fuel)
                startFuel += toadd
                ret += 1
            heapq.heappush(fuel, -refill)
        return ret 
