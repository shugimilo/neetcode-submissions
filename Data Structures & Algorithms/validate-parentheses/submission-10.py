class Solution:
    def isValid(self, s: str) -> bool:
        opening = set('([{')
        closing = set(')]}')
        print(f"s[0] = {s[0]}")
        if len(s) <= 1 or s[0] in closing:
            return False
        stack = list()
        for i in range(0, len(s)):
            if s[i] in opening:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                else:
                    topChar = stack[-1]
                    if (topChar == '(' and s[i] != ')') or (topChar == '[' and s[i] != ']') or (topChar == '{' and s[i] != '}'):
                        return False
                    else:
                        stack.pop()
        if stack:
            return False
        return True