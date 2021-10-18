class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
                graph[node].append(node.left)
                graph[node.left].append(node)
            if node.right:
                q.append(node.right)
                graph[node].append(node.right)
                graph[node.right].append(node)
        d = 0
        visited = {target}
        queue = deque([target])
        while queue:
            if d == k:
                return [n.val for n in queue]
            for _ in range(len(queue)):
                cur = queue.popleft()
                for node in graph[cur]:
                    if node not in visited:
                        visited.add(node)
                        queue.append(node)
            d += 1
        return []
