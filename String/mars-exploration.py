# https://www.hackerrank.com/challenges/mars-exploration/problem
# this function checks for every letter, x, in step of 3 of a string

def marsExploration(s):
    s = list(s)
    count = 0
    for i in range(0,len(s)):
        x = i % 3
        if x == 0 and s[i] !='S':
            count += 1
        elif x == 1 and s[i] != 'O':
            count += 1
        elif x == 2 and s[i] != 'S':
            count += 1
            
    return count 