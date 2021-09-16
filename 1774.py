class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        res = baseCosts[0]
        toppingCosts.sort()
        topping = [0]
        for t in toppingCosts:
            topping = [x+n*t for x in topping for n in range(3)]
        topping.sort()
        
        def closestSum(b_cost):
            tgt = target-b_cost
            if tgt <= 0: return b_cost
            l, r = 0, len(topping)-1
            while l <= r:
                mid = (l+r)//2
                if topping[mid] == tgt: return target
                elif topping[mid] < tgt: l = mid+1
                else: r = mid-1
            if r < 0 or (l < len(topping) and abs(tgt-topping[l]) < abs(tgt-topping[r])):
                return b_cost+topping[l]
            else:
                return b_cost+topping[r]
            
            
        for base in baseCosts:
            lower = closestSum(base)
            if abs(target-lower) < abs(target-res):
                res = lower
            elif abs(target-lower) > abs(target-res): continue
            else:
                res = min(res, lower)
        return res
