# https://www.hackerrank.com/challenges/gridland-metro/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridlandMetro function below.
# This code works for one list of track.
def gridlandMetro(n, m, k, track):
    i = 1
    j = 0
    units = 0
    while i < len(track):
        while j < k:
            if track[j][i]==track[j][i+1]:
                units += 1
            units += abs(track[j][i]-track[j][i+1])
    area = n * m
    res = area - units 
    return res 