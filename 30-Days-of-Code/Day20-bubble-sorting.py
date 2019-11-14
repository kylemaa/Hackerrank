# https://www.hackerrank.com/challenges/30-sorting/problem
#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swap_num = 0
counter = 0
# two loops to get the sorted array!
for x in range(len(a)-1):
    for y in range(x+1, len(a)):
        if a[x] > a[y]:
            temp = a[x]
            a[x] = a[y]
            a[y] = temp
            swap_num += 1
print('Array is sorted in {} swaps.'.format(swap_num))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[n-1]))
