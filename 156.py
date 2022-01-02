# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left:
            return root
        l, r = root.left, root.right
        newroot = self.upsideDownBinaryTree(l)
        l.left, l.right = r, root
        root.left = root.right = None
        return newroot
