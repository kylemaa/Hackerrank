
#!/bin/python3
# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    sub = 'hackerrank'
    k = 0
    for j in s:
        if j == sub[k]:
            k += 1
            if k == len(sub):
                return 'YES'
    return 'NO'

    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
