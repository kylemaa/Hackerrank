# https://www.hackerrank.com/challenges/counting-valleys/problem

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s): 
    count = 0
    level = 0
    for i in s: 
        if i == 'U':
            level += 1
        elif i == 'D':
            level -= 1
        if level == 0 and i == 'U':
            count += 1
    return count 
  
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()