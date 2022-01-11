# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def tran(root):
            if not root:
                return []
            return tran(root.left) + [root.val] + tran(root.right)
        
        def find(node, val):
            if not node:
                return 
            if node.val == val:
                return node
            return find(node.left, val) or find(node.right, val)
        
        arr = tran(root)
        a = b = None
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                if a is None:
                    a = arr[i-1]
                    b = arr[i]
                else:
                    b = arr[i]
                    break
        A = find(root, a)
        B = find(root, b)
        A.val, B.val = b, a
