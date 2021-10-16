class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for f,t in tickets:
            graph[f].append(t)
        for f in graph:
            graph[f].sort(reverse=True)
        stack = ['JFK']
        res = []
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            res.append(stack.pop())
        return res[::-1]
