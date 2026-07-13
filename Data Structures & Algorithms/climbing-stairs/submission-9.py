class Solution:
    def climbStairs(self, n: int) -> int:
        i = 0
        j = 1
        for _ in range(0, n):
            i, j = j, j+i

        return j