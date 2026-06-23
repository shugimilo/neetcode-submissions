class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        expected = sorted(heights, key=lambda x:x)
        for i in range(0, len(heights)):
            if expected[i] != heights[i]:
                count += 1

        return count