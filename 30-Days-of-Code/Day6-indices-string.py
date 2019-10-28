# https://www.hackerrank.com/challenges/30-review-loop/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_new_string(s):
    even =''
    odd =''
    for i in range(len(s)):
        if i % 2 == 0:
            even += s[i]
        else:
            odd += s[i]
    print(even+' '+odd)

t = int(input())
for _ in range(t):
    s = input()
    print_new_string(s)
