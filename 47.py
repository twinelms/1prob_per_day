class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        counter = Counter(nums)
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path)
                return
            for n in counter:
                if counter[n] > 0:
                    counter[n] -= 1
                    backtrack(path+[n])
                    counter[n] += 1
        
        backtrack([])
        return res
