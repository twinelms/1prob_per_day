class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        freq = set()
        res = 0
        for ch, f in counter.items():
            while f > 0 and f in freq:
                res += 1
                f -= 1
            if f > 0:
                freq.add(f)
        return res
