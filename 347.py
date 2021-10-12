class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        bucket=[[] for _ in range(len(nums))]
        for n,f in freq.items():
            bucket[f-1].append(n)
        res=[]
        for b in bucket[::-1]: res+=b
        return res[:k]
