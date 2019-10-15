#https://www.hackerrank.com/challenges/compare-the-triplets/problem
#!/bin/python3

import math
import os
import random
import re
import sys


def compareTriplets(a, b):
    apoint = bpoint = 0 
    arr = []
    for i in range (len(a)):
        if a[i] > b[i]:
            apoint += 1 
        elif a[i] < b[i]:
            bpoint += 1
    arr.append(apoint)
    arr.append(bpoint)
    return arr


    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()