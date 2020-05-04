class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = last = 0
        chars = set()
        while last < len(s):
            if s[last] not in chars:
                chars.add(s[last])
                last += 1
                longest = max(longest, len(chars))
            else:
                if s[start] in chars:
                    chars.remove(s[start])
                start += 1
        return longest
