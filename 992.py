class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        i = j = start = res = 0
        while j < len(nums):
            count[nums[j]] += 1
            if count[nums[j]] == 1:
                k -= 1
            if k < 0:
                count[nums[i]] -= 1
                k += 1
                i += 1
                start = i
            if k == 0:
                while count[nums[i]] != 1:
                    count[nums[i]] -= 1
                    i += 1
                res += i-start+1
            j += 1
        return res
