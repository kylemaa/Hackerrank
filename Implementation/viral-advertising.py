# https://www.hackerrank.com/challenges/strange-advertising/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    shared = 5 
    likes = 0
    for i in range(n):
        likes += shared//2 
        shared = (shared//2) * 3
    
    return likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
