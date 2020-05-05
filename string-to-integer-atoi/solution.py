import re
import string

class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MIN = (-1 << 31)
        INT_MAX = (1 << 31) - 1 
        str = str.strip()
        if len(str) == 0: return 0
        if str[0] in string.ascii_lowercase:
            return 0
        bit = None
        ans = ''
        for i in range(len(str)):
            if i == 0 and str[i] in ['-', '+']:
                bit = str[i]
                continue
            if str[i].isdigit(): ans += str[i]
            else: break
        if not ans: return 0
        ans = int(ans)
        if bit == '-': ans = -ans
        if INT_MIN <= ans <= INT_MAX: return ans
        return INT_MIN if ans < INT_MIN else INT_MAX
