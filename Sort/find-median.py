#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the findMedian function below.
def findMedian(arr):
    a = sorted(arr)
    if len(a) % 2 ==0:
        median_index = (len(a)/2)-1
    elif len(a) % 2 != 0:
        median_index = len(arr)//2
    return a[median_index]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
