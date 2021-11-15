class Codec:

    def serialize(self, root):  # preorder
        def dfs(node):
            if not node:
                return '*'
            return str(node.val)+' '+dfs(node.left)+' '+dfs(node.right)
        return dfs(root)

    def deserialize(self, data):
        data = deque(data.split())
        def dfs():
            if not data: return
            cur = data.popleft()
            if cur == '*':
                return None
            node = TreeNode(int(cur))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
