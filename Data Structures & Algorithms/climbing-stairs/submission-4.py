class Solution:
    def climbStairs(self, n: int) -> int:
        fibonacci = []

        fibonacci.append(1)
        fibonacci.append(2)

        i = 1

        while i <= n:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
            i += 1

        return fibonacci[n-1] 