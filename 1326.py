    def minTaps(self, n: int, ranges: List[int]) -> int:
        cover = [0]*(n+1)
        # transform the input, the question becomes similar to jump game
        for i in range(n+1):
            left = max(0, i-ranges[i])
            right = i+ranges[i]
            cover[left] = max(cover[left], right-left)
        reach = n_reach = res = 0
        for i, r in enumerate(cover):
            if reach < i:
                res += 1
                if n_reach < i: return -1
                reach = n_reach
            n_reach = max(n_reach, i+r)
        return res
