class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        isPositive = True if x > 0 else False

        reverseX = 0

        x = abs(x)

        while x >= 10:
            whole = x // 10
            modulo = x % 10

            reverseX += modulo
            reverseX *= 10

            x = whole

        reverseX += x

        if reverseX >= (2**31) - 1 or -reverseX <= -(2**31):
            return 0

        if isPositive:
            return reverseX
        else:
            return -reverseX
        