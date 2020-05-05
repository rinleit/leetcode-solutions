class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        i = 0
        while i < len(s):
            if s[i] in brackets :
                stack.append(s[i])
            else:
                if not stack: return False
                if brackets[stack.pop()] != s[i]:
                    return False
            i += 1
        return True if not stack else False
