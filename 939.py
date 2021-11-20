class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0]*x[0]+x[1]*x[1])
        p = set()
        for x,y in points:
            p.add((x,y))
        res = float('inf')
        for i, (x, y) in enumerate(points):
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                if x < x2 and y < y2 and (x, y2) in p and (x2, y) in p:
                    res = min(res, (x2-x)*(y2-y))
                    break
        return res if res != float('inf') else 0
