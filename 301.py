class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isvalid(s):
            stack = []
            for c in s:
                if c == '(':
                    stack.append(c)
                elif c == ')':
                    if not stack: return False
                    stack.pop()
            return not stack
        
        cur = {s}
        while True:
            res = []
            for s in cur:
                if isvalid(s): res.append(s)
            if res:
                return res
            new = set()
            for s in cur:
                for i in range(len(s)):
                    if s[i] in '()':
                        new.add(s[:i]+s[i+1:])
            cur = new
