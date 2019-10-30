# https://www.hackerrank.com/challenges/sherlock-and-array/problem
#!/bin/python3

import math
import os
import random
import re
import sys

def balancedSums(arr):
    sumofarr = sum(arr)
    left = 0 
    for i in range(len(arr)):
        current = arr[i]
        sumofarr -= current
        if left == sumofarr:
            return 'Yes'
        left += current
    return 'No'