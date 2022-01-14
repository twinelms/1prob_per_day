class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy = [float('inf')]*(1+k)
        buysell = [0]*(1+k)
        for p in prices:
            for t in range(1,k+1):
                buy[t] = min(buy[t], p-buysell[t-1])
                buysell[t] = max(buysell[t], p-buy[t])
        return buysell[k]
