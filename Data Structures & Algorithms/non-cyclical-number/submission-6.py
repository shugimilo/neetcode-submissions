class Solution:
    def findNext(self, n: int) -> int:
        newN = 0
        while n >= 10:
            newN += (n%10)**2
            n = n//10
        newN += n**2
        return newN

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        m = self.findNext(self.findNext(n))
        while n != m:
            if n == 1 or m == 1:
                return True
            n = self.findNext(n)
            m = self.findNext(self.findNext(m))
        return False