class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        self.res = 0
        def findsum(node, cur):
            if not node: return
            cur += node.val
            self.res += dic[cur-targetSum]
            dic[cur] += 1
            findsum(node.left, cur)
            findsum(node.right, cur)
            dic[cur] -= 1  # avoid affecting other subtrees
        findsum(root, 0)
        return self.res
