class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        weighted = unweighted = 0
        queue = deque([nestedList])
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                for ni in cur:
                    if ni.isInteger():
                        unweighted += ni.getInteger()
                    else:
                        queue.append(ni.getList())
            weighted += unweighted
        return weighted
