class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i,j=0,0
        while i==0 or i!=j:
            i=nums[i]
            j=nums[nums[j]]
        i=0
        while i!=j:
            i=nums[i]
            j=nums[j]
        return i
        
