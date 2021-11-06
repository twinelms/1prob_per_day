class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([]) # store only idx, nums[i] in descending order
        res = []
        for i, n in enumerate(nums):
            while q and nums[q[-1]] <= n:
                q.pop()
            q.append(i)
            if i - q[0]+1 > k:
                q.popleft()
            if i >= k-1: res.append(nums[q[0]])
        return res
