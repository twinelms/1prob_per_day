class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        ref = [(v, i) for i, v in enumerate(nums)]
        
        def merge(A, B):
            ret = [(0,0)]*(len(A)+len(B))
            i = j = 0
            for k in range(len(ret)):
                if j >= len(B) or (i < len(A) and A[i][0] <= B[j][0]):
                    ret[k] = A[i]
                    res[A[i][1]] += k-i
                    i += 1
                else:
                    ret[k] = B[j]
                    j += 1
            return ret
        
        def sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr)//2
            A = sort(arr[:mid])
            B = sort(arr[mid:])
            return merge(A, B)
        
        sort(ref)
        return res
