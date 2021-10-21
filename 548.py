class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        n = len(nums)
        s = [0]*n
        for i in range(n):
            s[i] = s[i-1]+nums[i]
        # split the array into halves, find j first
        for j in range(3,n):
            target = set()
            for i in range(1,j-1):
                if s[i-1] == s[j-1]-s[i]:
                    target.add(s[i-1])
            for k in range(j+2,n-1):
                if s[k-1]-s[j] == s[-1]-s[k] and s[-1]-s[k] in target:
                    return True
        return False
