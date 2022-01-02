# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        res = 0
        while stack:
            node, path = stack.pop()
            res = max(res, path)
            if node.left:
                stack.append(
                    (node.left, path+1 if node.left.val == node.val+1 else 1)
                )
            if node.right:
                stack.append(
                    (node.right, path+1 if node.right.val==node.val+1 else 1)
                )
        return res
