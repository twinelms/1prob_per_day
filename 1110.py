class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        roots = {root}
        q = deque([(root, None)])
        to_delete = set(to_delete)
        while to_delete:
            cur, parent = q.popleft()
            if cur.left:
                q.append((cur.left, cur))
            if cur.right:
                q.append((cur.right, cur))
            if cur.val in to_delete:
                roots.discard(cur)
                to_delete.remove(cur.val)
                if cur.left:
                    roots.add(cur.left)
                    cur.left = None
                if cur.right:
                    roots.add(cur.right)
                    cur.right = None
                if parent:
                    if cur == parent.left:
                        parent.left = None
                    else:
                        parent.right = None
        return list(roots)
