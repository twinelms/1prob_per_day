class Solution:
    def maxProfit(self, a: List[int]) -> int:
        buy1 = float('inf')
        buy1sell1 = 0
        buy2 = float('inf')
        buy2sell2 = 0
        for p in a:
            buy1 = min(buy1, p)
            buy1sell1 = max(buy1sell1, p-buy1)
            buy2 = min(buy2, p-buy1sell1)
            buy2sell2 = max(buy2sell2, p-buy2)
        return buy2sell2
