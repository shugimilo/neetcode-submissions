class Solution:
    def isValid(self, s: str) -> bool:
        opening = set('([{')
        closing = set(')]}')
        print(f"s[0] = {s[0]}")
        if len(s) <= 1 or s[0] in closing:
            return False
        stack = list()
        top = -1
        for i in range(0, len(s)):
            if s[i] in opening:
                top += 1
                stack.append(s[i])
            else:
                if top < 0:
                    return False
                else:
                    topChar = stack[top]
                    if (topChar == '(' and s[i] != ')') or (topChar == '[' and s[i] != ']') or (topChar == '{' and s[i] != '}'):
                        return False
                    else:
                        stack.pop()
                        top -= 1
        if top != -1:
            print(f"Returning False because top = {top}")
            return False
        return True