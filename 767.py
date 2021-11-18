class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        h = []
        res = []
        for c, freq in count.items():
            heapq.heappush(h, [-freq, c])
        pre = [0, '']
        while h:
            f, cur = heapq.heappop(h)
            res.append(cur)
            f += 1
            if pre[0]:
                heapq.heappush(h, pre)
            pre = [f, cur]
        return ''.join(res) if len(res) == len(s) else ''
