class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return float(1)
        positive = False if n < 0 else True
        n = abs(n)

        #print(f"x: {x}, n: {n}")

        i=0
        res=x
        while n > 1:
            res*=x
            n -= 1
            #print(f"\titeration: {i}, updated res to {res} and n to {n}")
            i+=1

        if not positive:
            res = 1/res
        return res