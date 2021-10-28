class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # use prefix_sum
        # find the smallest and latest val that meets requirement => deque !
        q = deque([(-1, 0)])
        res, cur = float('inf'), 0
        for i, n in enumerate(nums):
            cur += n
            while q and cur-q[0][1] >= k:
                res = min(res, i-q.popleft()[0])
            while q and cur <= q[-1][1]:
                q.pop()
            q.append((i, cur))
        return res if res != float('inf') else -1
