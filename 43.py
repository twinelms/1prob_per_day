class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m,n = len(num1), len(num2)
        res = [0]*(m+n)
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                temp = res[i+j+1]+(ord(num1[j])-ord('0'))*(ord(num2[i])-ord('0'))
                res[i+j+1] = temp%10
                res[i+j] += temp//10
        idx = 0
        while idx < m+n-1 and res[idx] == 0:
            idx += 1
        return ''.join(map(str, res[idx:]))
