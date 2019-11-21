#!/bin/python3
# Print an alphabetically-ordered list of first names for every user with a gmail account. 
# Each name must be printed on a new line
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    lst=[]
    for a0 in range(N):
        firstName, emailID = [str(s) for s in input().split()]
        if re.search('@gmail\.com$', emailID):
            lst.append(firstName)
    print(*sorted(lst), sep='\n')
