class Solution:
    def myPow(self, x: float, n: int) -> float:
        positive = False if n < 0 else True
        n = abs(n)

        res=float(1)
        while n >= 1:
            res*=x
            n -= 1

        if not positive:
            res = 1/res
        return res