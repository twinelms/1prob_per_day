class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float('inf')]
        res = 0
        for n in arr:
            while stack[-1] <= n:
                remove = stack.pop()
                res += remove*min(stack[-1], n)
            stack.append(n)
        while len(stack) > 2:
            res += stack.pop()*stack[-1]
        return res

    
class Solution_1:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = []
        res = 0
        for n in arr:
            while stack and stack[-1] <= n:
                to_remove = stack.pop()
                res += to_remove*min(n, stack[-1]) if stack else to_remove*n
            stack.append(n)
        while len(stack) > 1:
            res += stack.pop()*stack[-1]
        return res
