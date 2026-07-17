class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            digits2 = []
            while n >= 10:
                digits2.append((n%10)**2)
                n = n//10
            digits2.append(n**2)
            n = 0
            for digit2 in digits2:
                n += digit2
            if n == 1:
                return True
        return False