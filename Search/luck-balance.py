# https://www.hackerrank.com/challenges/luck-balance/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    luck = 0 
    important = []
    for val in (contests):
        if val[1] == 1:
            important.append(val[0])
        elif val[1]== 0:
            luck += val[0]
    important = sorted(important, reverse=True)
    j = 0
    while j < k:
        luck += important[j]
        j +=1
    while j < len(important):
        luck -= important[j]
        j+=1
    return luck
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
