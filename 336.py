class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        reverse = {}
        for i,w in enumerate(words):
            reverse[w] = i
        res = []
        for i,w in enumerate(words):
            if w[::-1] in reverse and reverse[w[::-1]] != i:
                res.append([reverse[w[::-1]], i])
            for k in range(1, len(w)):
                prefix, suffix = w[:k], w[k:]
                if prefix == prefix[::-1] and suffix[::-1] in reverse:
                    res.append([reverse[suffix[::-1]], i])
                if suffix == suffix[::-1] and prefix[::-1] in reverse:
                    res.append([i, reverse[prefix[::-1]]])
            if "" in reverse and w and w == w[::-1]:
                res.append([i, reverse[""]])
                res.append([reverse[""], i])
        return res
