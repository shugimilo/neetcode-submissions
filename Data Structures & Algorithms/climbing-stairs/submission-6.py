class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        i = 1
        j = 2
        for _ in range(0, n-2):
            i, j = j, j+i

        return j