class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        bold = [False]*len(s)
        for word in words:
            i = s.find(word)
            while i != -1:
                for k in range(i, i+len(word)):
                    bold[k] = True
                i = s.find(word, i+1)
        i = 0
        res = []
        while i < len(bold):
            if bold[i] and (not i or not bold[i-1]):
                res.append('<b>')
            res.append(s[i])
            if bold[i] and ((i+1<len(bold) and not bold[i+1]) or i == len(bold)-1):
                res.append('</b>')
            i += 1
        return ''.join(res)
