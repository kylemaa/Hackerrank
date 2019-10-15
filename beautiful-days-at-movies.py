# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.

def beautifulDays(i, j, k):
    lst = []
    for num in range (i,j+1):
        m = num - int(str(num)[::-1])
        if m % k == 0:
            lst.append(m)
    return len(lst)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
