class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n, res = len(nums), float('inf')
        
        def allSum(arr):
            sums = {0}
            for num in arr:
                sums |= {s+num for s in sums} 
            return sorted(sums)
        
        subsum1 = allSum(nums[:n//2])
        subsum2 = allSum(nums[n//2:])
        for sum1 in subsum1:
            idx = bisect.bisect_left(subsum2, goal-sum1)
            # corner case: idx = 0 or len(subsum2)
            if idx < len(subsum2):
                res = min(res, abs(goal-sum1-subsum2[idx]))  
            if idx > 0:
                res = min(res, abs(goal-sum1-subsum2[idx-1]))
        return res
