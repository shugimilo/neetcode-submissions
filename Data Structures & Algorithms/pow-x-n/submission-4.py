class Solution:
    def recursion(self, x: float, n: int) -> float:
        if n == 0:
            return float(1)
        if n % 2 == 0:
            half = self.recursion(x, n//2)
            return half*half
        else:
            return x*self.recursion(x, n-1)

    def myPow(self, x: float, n: int) -> float:
        negative = True if n < 0 else False
        res = self.recursion(x, abs(n))

        if negative:
            res = 1/res
        return res