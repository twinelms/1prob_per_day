class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        person = defaultdict(int)
        for f, t, amount in transactions:
            person[f] -= amount
            person[t] += amount
        balances = []
        for p in person:
            if person[p]:
                balances.append(person[p])
        balances.sort()
        # greedy
        i, j, res = 0, len(balances)-1, 0
        while i < j and balances[i] < 0 and balances[j] > 0:
            if balances[i] + balances[j] == 0:
                balances[i] = 0
                balances[j] = 0
                res += 1
                i += 1
                j -= 1
            elif abs(balances[i]) > abs(balances[j]):
                i += 1
            else:
                j -= 1            
        
        def dfs(idx):
            if idx == len(balances):
                return 0
            if balances[idx] == 0:
                return dfs(idx+1)
            minTran = float('inf')
            for i in range(idx+1, len(balances)):
                if balances[i]*balances[idx] < 0:
                    balances[i] += balances[idx]
                    minTran = min(minTran, 1+dfs(idx+1))
                    balances[i] -= balances[idx]
            return minTran
        
        return res+dfs(0)
