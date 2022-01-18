# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            smaller = root.left
            while smaller and smaller.right:
                smaller = smaller.right
            root.val = smaller.val
            root.left = self.deleteNode(root.left, smaller.val)
        return root
