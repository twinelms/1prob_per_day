class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights += [0]
        stack, res = [-1], 0
        for i, h in enumerate(heights):
            while heights[stack[-1]] > h:
                cur = stack.pop()
                res = max(res, heights[cur]*(i-stack[-1]-1))
            stack.append(i)
        return res
