# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        palind = ''  # Empty string to store palindromic string
        for i in range(len(s)):  # starting from the beginning
            for j in range(len(s), i, -1):  # starting from the ending
                if len(palind) >= j-i:
                    break
                elif s[i:j] == s[i:j][::-1]:
                    palind = s[i:j]
                    break
        return palind
