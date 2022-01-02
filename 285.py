# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        cur = root
        pre = None
        while cur:
            if cur.val > p.val:
                pre = cur
                cur = cur.left
            else:
                cur = cur.right
        return pre
   
