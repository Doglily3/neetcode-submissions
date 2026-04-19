class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        biggest = 0
        while i<j:
            size = min(heights[i],heights[j]) * (j-i)
            biggest = max(size, biggest)
            if heights[i]>heights[j]:
                j -= 1
            else:
                i += 1
        return biggest
            