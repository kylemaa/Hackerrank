# https://www.hackerrank.com/challenges/funny-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    s_array = [ord(c) for c in s]
    r_array = [ord(c) for c in s[::-1]]
    for i in range (len(s_array)-1):
        s_value = abs(s_array[i] - s_array[i+1])
        r_value = abs(r_array[i] - r_array[i+1])
        if s_value != r_value:
            return 'Not Funny'
            
    return 'Funny'


     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
