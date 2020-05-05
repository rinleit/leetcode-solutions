class Solution1:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        longest = 0
        indices = [0,0]
        dp = [[0 for _ in range(length)] for _ in range(length)]
        for L in range(1,length+1):
            for i in range(0,length-L+1):
                j = i+L-1 
                if i == j:
                    dp[i][j] = 1 
                elif s[i] == s[j]:
                    if abs(i-j) == 1:
                        dp[i][j] = 2 
                    elif dp[i+1][j-1] > 0:
                        dp[i][j] = dp[i+1][j-1]  + 2
                    else:
                        dp[i][j] = 0
                if dp[i][j] > longest:
                    longest = dp[i][j]
                    indices[0] = i 
                    indices[1] = j
        return s[indices[0]:indices[1]+1]

class Solution2:
    def longestPalindrome(self, s: str) -> str:
        m = ''  # Memory to remember a palindrome
        for i in range(len(s)):  # i = start, O = n
            for j in range(len(s), i, -1):  # j = end, O = n^2
                if len(m) >= j-i:  # To reduce time
                    break
                elif s[i:j] == s[i:j][::-1]:
                    m = s[i:j]
                    break
        return m
