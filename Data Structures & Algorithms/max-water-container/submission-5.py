class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        maxArea = 0

        i = 0
        j = len(heights)-1

        while i < j:
            current = min(heights[i], heights[j])*abs(i-j)
            if maxArea < current:
                maxArea = current
            if heights[i] < heights[j]:
                i+=1
            elif heights[i] > heights[j]:
                j-=1
            else:
                i+=1
                j-=1

        return maxArea