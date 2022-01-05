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
        
class Solution_1:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while slow != fast or not slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
