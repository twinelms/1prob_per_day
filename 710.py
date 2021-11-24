class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.bl = {}
        self.length = n-len(blacklist)
        blacklist = set(blacklist)
        k = self.length
        for i in blacklist:
            while k in blacklist:
                k += 1
            if i < self.length:
                self.bl[i] = k
                k += 1

    def pick(self) -> int:
        idx = random.randint(0, self.length-1)
        if idx in self.bl: 
            return self.bl[idx]
        return idx
