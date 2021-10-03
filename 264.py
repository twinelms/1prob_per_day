class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        p2 = p3 = p5 = 0
        while len(ugly) < n:
            u2, u3, u5 = ugly[p2]*2, ugly[p3]*3, ugly[p5]*5
            cur = min(u2, u3, u5)
            if cur == u2:
                p2 += 1
            if cur == u3: # !parallel if! to avoid duplicates
                p3 += 1
            if cur == u5:
                p5 += 1
            ugly.append(cur)
        return ugly[-1]
