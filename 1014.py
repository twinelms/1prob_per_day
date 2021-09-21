class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        cur_max, res = values[0], float('-inf')
        for v in values[1:]:
            cur_max -= 1
            res = max(res, cur_max+v)
            cur_max = max(cur_max, v)
        return res
