# https://www.hackerrank.com/challenges/30-binary-numbers/problem
#!/bin/python3


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary = []
    while n > 0:
        remainder = n%2
        binary.append(remainder)
        n = n//2
    count = 0
    maximum = 0
    for i in binary: 
        if i == 1:
            count += 1
            if maximum <= count:
                maximum = count 
            # else: 
            #     pass
        if i == 0:
            count = 0
    print(maximum)
        
    

    
    
