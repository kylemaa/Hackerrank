# https://www.hackerrank.com/challenges/the-birthday-bar/problem
def birthday(s, d, m):
    res = 0
    for i in range(len(s)):
        if sum(s[i:m+i]) == d:
            res += 1
    return res
