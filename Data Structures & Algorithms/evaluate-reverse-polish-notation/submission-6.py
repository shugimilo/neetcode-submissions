from math import ceil, floor

class Solution:
    def apply(self, a: int, b: int, operator: str) -> int:
        print(f"received a: {a}, b: {b}, operator: {operator}")
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        else:
            if a / b > 0:
                return floor(a/b)
            else:
                return ceil(a/b)

    def evalRPN(self, tokens: List[str]) -> int:
        buffer = []
        operators = set('+-*/')

        for token in tokens:
            if token not in operators:
                buffer.append(int(token))
            else:
                b = buffer.pop()
                a = buffer.pop()
                buffer.append(self.apply(a, b, token))

        return buffer.pop()
