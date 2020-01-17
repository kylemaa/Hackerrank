class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        l, r = s, ""
        rev_s = s[::-1]

        while(rev_s != r + l and n > 1):
            r += l[-1]
            l = l[:n - 1]
            n -= 1
        return r + s
