class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def pick(self, target: int) -> int:
        count = 0
        for i,n in enumerate(self.nums):
            if n == target:
                if random.randint(0,count) == 0:   # reservoir sampling
                    res = i
                count += 1
        return res
