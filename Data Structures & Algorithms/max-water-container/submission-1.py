class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        maxArea = 0

        for i in range(0, len(heights)):
            for j in range(0, len(heights)):
                if j == i or heights[j] < heights[i]:
                    continue
                else:
                    area = abs(i-j)*min(heights[i], heights[j])
                    if area > maxArea:
                        maxArea = area

        return maxArea