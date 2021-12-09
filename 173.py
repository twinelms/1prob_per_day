class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        cur = self.stack.pop()
        ret = cur.val
        cur = cur.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return ret

    def hasNext(self) -> bool:
        return self.stack
        
