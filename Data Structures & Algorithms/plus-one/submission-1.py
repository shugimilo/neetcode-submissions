class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        while digits and carry:
            digit = digits.pop()
            print(f"digit before: {digit}")
            digit = digit + carry
            print(f"digit after: {digit}")
            if digit != 10:
                res.append(digit)
                print(f"appended {digit} to res: {res}")
                print(f"exiting, remaining digits: {digits}")
                carry = 0
            else:
                print(f"appending 0 to res...")
                res.append(0)
                print(f"res: {res}")
            print(f"\n")

        if digits:
            digits.reverse()
            res += digits
        if carry:
            res.append(1)

        res.reverse()
        return res


