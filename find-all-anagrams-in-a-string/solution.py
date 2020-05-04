from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if len(s)<len(p) or not(set(s)>=set(p)):
            return ans
        p_c = Counter(p)
        p_n = len(p)
        s_n = len(s)
        for i in range(s_n - p_n + 1):
            if Counter(s[i:i+p_n]) == p_c:
                ans += [i]
        return ans
