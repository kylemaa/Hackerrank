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
            calulate_abs = abs(a[i+1] - a[i])
            if smallest > calulate_abs:
                smallest = calulate_abs
                # TODO: use dictionary to keep track of which 2 have the same smallest
                ret_a = [a[i], a[i+1]]
    # calculated the right smallest
    # print(smallest)
