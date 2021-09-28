class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i, j, m, n = 0, 0, len(firstList), len(secondList)
        while i < m and j < n:
            l = max(firstList[i][0], secondList[j][0])
            r = min(firstList[i][1], secondList[j][1])
            if l <= r: res.append([l,r])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return res
