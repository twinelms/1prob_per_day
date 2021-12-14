class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 1
        q = deque([(root, 1)])
        while q:
            res = max(res, q[-1][1]-q[0][1]+1)
            new = deque([])
            for _ in range(len(q)):
                node, i = q.popleft()
                if node.left:
                    new.append((node.left, 2*i-1))
                if node.right:
                    new.append((node.right, 2*i))
            q = new
        return res
