class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            rightmost = root.left
            while rightmost.right:
                rightmost = rightmost.right
            root.val = rightmost.val
            root.left = self.deleteNode(root.left, rightmost.val)
        return root
