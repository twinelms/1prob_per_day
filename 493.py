class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        pairs = 0
        def sort(l,r):
            nonlocal pairs
            if l == r:
                return []
            if l+1 == r:
                return [nums[l]]
            m = (l+r)//2
            A = sort(l, m)
            B = sort(m, r)
            i = 0
            for x in A:
                while i < len(B) and B[i] < x/2:
                    i += 1
                pairs += i
            res = [0]*(len(A)+len(B))
            i = j = 0
            for k in range(len(A)+len(B)):
                if j >= len(B) or i < len(A) and A[i] < B[j]:
                    res[k] = A[i]
                    i += 1
                else:
                    res[k] = B[j]
                    j += 1
            return res
        
        sort(0, len(nums))
        return pairs
