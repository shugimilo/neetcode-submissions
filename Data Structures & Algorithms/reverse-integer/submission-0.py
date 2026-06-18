def isPositiveInt(x):
    return x > 0

class Solution:
    def reverse(self, x: int) -> int:
        isPositive = isPositiveInt(x)

        reverseX = 0

        x = abs(x)

        while x >= 10:
            whole = x // 10
            modulo = x % 10

            reverseX += modulo
            reverseX *= 10

            x = whole

        reverseX += x

        if reverseX >= (2**31) - 1 or reverseX <= -(2**31):
            return 0

        if isPositive:
            return reverseX
        else:
            return -reverseX
        