#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    # Sort the array
    a = sorted(arr)
    smallest = max(a)
    ret_a = []
    for i in range(len(a)):
        # If index is smaller than the last index in this array a
        if i < len(a)-2:
            calulate_abs = a[i+1] - a[i]
            if smallest > calulate_abs:
                ret_a = []
                ret_a.append(a[i])
                ret_a.append(a[i+1])
                smallest = abs(calulate_abs)
            elif smallest == calulate_abs:
                ret_a.append(a[i])
                ret_a.append(a[i+1])
    return ret_a 


