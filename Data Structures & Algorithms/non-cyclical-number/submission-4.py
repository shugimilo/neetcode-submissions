class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            newN = 0
            while n >= 10:
                newN += (n%10)**2
                n = n//10
            newN += n**2
            if newN == 1:
                return True
            else:
                n = newN
        return False