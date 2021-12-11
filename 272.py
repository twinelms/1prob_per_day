class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        stack = []
        h = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            heapq.heappush(h, (-abs(target-cur.val), cur.val))
            if len(h) > k:
                heapq.heappop(h)
            cur = cur.right
        return [x[1] for x in h]
