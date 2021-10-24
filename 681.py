class Solution:
    def nextClosestTime(self, time: str) -> str:
        h, m = time.split(':')
        digits = sorted(set(h+m))
        doubles = [x+y for x in digits for y in digits]
        i = bisect.bisect_right(doubles, m)
        if i < len(doubles) and int(doubles[i]) < 60:
            return h+':'+doubles[i]
        j = bisect.bisect_right(doubles, h)
        if j < len(doubles) and int(doubles[j]) < 24:
            return doubles[j]+':'+doubles[0]
        return doubles[0]+':'+doubles[0]
        
