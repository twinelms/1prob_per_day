class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        i = 0
        stack = []
        res = []
        while head:
            while stack and head.val > stack[-1][1]:
                idx, val = stack.pop()
                res[idx] = head.val
            res.append(0)
            stack.append((i, head.val))
            head = head.next
            i += 1
        return res
