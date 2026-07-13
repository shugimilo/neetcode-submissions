class Solution:
    def climbStairs(self, n: int) -> int:
        i = 1
        j = 2
        for _ in range(0, n-1):
            tmp = j
            j = i + tmp
            i = tmp

        return i