from math import floor, ceil

class Solution:
    def apply(self, a: int, b: int, operator: str) -> int:
        print(f"received a: {a}, b: {b}, operator: {operator}")
        if operator == '+':
            res = a + b
        elif operator == '-':
            res = a - b
        elif operator == '*':
            res =  a * b
        else:
            if a / b < 0:
                res = ceil(a/b)
            else:
                res = floor(a/b)
        print(f"returning result: {res}")
        return res

    def evalRPN(self, tokens: List[str]) -> int:
        buffer = []
        operators = set('+-*/')

        for token in tokens:
            #print(f"buffer: {buffer}")
            if token not in operators:
                print(f"\tappending number: {token}")
                buffer.append(int(token))
            else:
                b = buffer.pop()
                a = buffer.pop()
                buffer.append(self.apply(a, b, token))
                #print(f"\tbuffer after operation: {buffer}")

        return buffer.pop()