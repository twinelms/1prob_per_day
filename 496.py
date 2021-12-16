class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        for i, n in enumerate(nums1):
            dic[n] = i
        ans = [-1]*len(nums1)
        stack = []
        for i, n in enumerate(nums2):
            while stack and n > nums2[stack[-1]]:
                small = nums2[stack.pop()]
                if small in dic:
                    ans[dic[small]] = n
            stack.append(i)
        return ans
