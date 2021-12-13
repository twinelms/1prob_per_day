class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        count = defaultdict(list)
        for i, n in enumerate(nums):
            count[n].append(i)
        res = [-1]*len(queries)
        for i, (l,r) in enumerate(queries):
            pre = None
            ans = float('inf')
            for v in range(1, 101):
                idx1, idx2 = bisect.bisect_left(count[v], l), bisect.bisect_right(count[v],r)
                if idx1 != idx2:
                    if pre:
                        ans = min(ans, v-pre)
                    pre = v
            if ans != float('inf'):
                res[i] = ans
        return res
