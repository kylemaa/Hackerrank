#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    zeros_arr = [0]*(len(arr)+len(brr))
    ret_arr = []
    for i in arr:
        zeros_arr[i] -= 1
    for i in brr:
        zeros_arr[i] += 1
    for j in range(len(zeros_arr)):
        if zeros_arr[j] > 0:
            ret_arr.append(j)
    return ret_arr
    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
