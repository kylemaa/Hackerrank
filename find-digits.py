# https://www.hackerrank.com/challenges/find-digits/problem
# !/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    lst_holder = []
    num = []
    for i in str(n):
        lst_holder.append(int(i))
    for j in lst_holder: 
        if j !=0 and n % j == 0:
            num.append(j)
    return len(num)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
