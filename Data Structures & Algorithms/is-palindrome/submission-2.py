class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
        s = s.lower()
        print(s)
        string = list(s)
        i = 0
        j = len(string) - 1
        while i < j:
            if string[i] not in alphanumeric:
                i+=1
                continue
            if string[j] not in alphanumeric:
                j-=1
                continue
            if string[i] != string[j]:
                print(f"string[i] = string[{i}] = {string[i]}\nIS NOT EQUAL TO\nstring[j] = string[{j}] = {string[j]}")
                return False
            else:
                print(f"string[{i}] = string[{j}]\n{string[i]} = {string[j]}")
            i+=1
            j-=1
        return True