class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod = {}
        mod[0] = -1
        cur = 0
        for i, n in enumerate(nums):
            cur = (cur+n)%k
            if cur not in mod:
                mod[cur] = i
            elif mod[cur]+2 <= i: # mininum size of subarray is 2
                return True
        return False
