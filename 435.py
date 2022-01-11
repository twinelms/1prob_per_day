class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res = 0
        end = intervals[0][1]
        for x, y in intervals[1:]:
            if end <= x:
                end = y
            else:
                res += 1
        return res
    
class Solution2:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ret = 0
        pre = float('-inf')
        for a, b in intervals:
            if pre <= a:
                pre = b
            else:
                ret += 1
                pre = min(pre, b)
        return ret
