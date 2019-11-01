# https://www.hackerrank.com/challenges/lisa-workbook/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    page = 1 
    special = 0
    leftover = 0
    for i in range(n):
        count = leftover
        for j in range (1, arr[i]+1):
            count += 1
            if j == page:
                special += 1
        if count >= k:
            #Have to increment this page right if count is more than 2x k
            page += 1
            leftover = count - k
        if count < k:
            page += 1
            leftover = 0

    return special
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
