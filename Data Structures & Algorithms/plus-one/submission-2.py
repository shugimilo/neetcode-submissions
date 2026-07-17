class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        while digits and carry:
            digit = digits.pop()
            digit = digit + carry
            if digit != 10:
                res.append(digit)
                carry = 0
            else:
                res.append(0)

        if digits:
            digits.reverse()
            res += digits
        if carry:
            res.append(1)

        res.reverse()
        return res


