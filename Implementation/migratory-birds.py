# https://www.hackerrank.com/challenges/migratory-birds/problem
import math
import os
import random
import re
import sys

# this is a counting sort problem 
def migratoryBirds(arr):
    holder = [0]*6
    for i in arr:
        holder[i] += 1
    
    res = holder.index(max(holder))
    return res



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()