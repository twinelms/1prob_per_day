class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def left(node):
            if not node or (not node.left and not node.right):
                return
            res.append(node.val)
            if node.left:
                left(node.left)
            else:
                left(node.right)
        def leaf(node):
            if not node:
                return
            if not node.left and not node.right:
                res.append(node.val)
                return
            leaf(node.left)
            leaf(node.right)
        def right(node):
            if not node or (not node.left and not node.right):
                return
            if node.right:
                right(node.right)
            else:
                right(node.left)
            res.append(node.val)
            
        res = [root.val]
        left(root.left)
        leaf(root.left)
        leaf(root.right)
        right(root.right)
        return res
