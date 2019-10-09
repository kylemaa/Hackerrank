#https://www.hackerrank.com/challenges/plus-minus/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr, n):
    pos_count= neg_count = zero_count=0
    for i in arr:
        if i > 0:
            pos_count += 1 
        elif i < 0:
            neg_count += 1
        else:
            zero_count += 1
    print (pos_count/n)
    print (neg_count/n)
    print (zero_count/n)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)


