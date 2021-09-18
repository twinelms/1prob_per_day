class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        pre, use, unuse = None, 0, 0
        for num in sorted(count.keys()):
            if num-1 == pre:
                use, unuse = unuse+num*count[num], max(use, unuse)
            else:
                use, unuse = max(use, unuse)+num*count[num], max(use, unuse)             
            pre = num
        return max(use, unuse)
