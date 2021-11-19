class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        i = i0 = j = res = 0
        while j < len(nums):
            count[nums[j]] += 1
            if count[nums[j]] == 1:
                k -= 1
            if k < 0:
                count[nums[i]] -= 1
                i += 1
                i0 = i
                k += 1
            if k == 0:
                while count[nums[i]] > 1:
                    count[nums[i]] -= 1
                    i += 1
                res += (i-i0)+1
            j += 1
        return res
