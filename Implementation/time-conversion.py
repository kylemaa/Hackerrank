# https://www.hackerrank.com/challenges/time-conversion/problem
#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    int_hr = int(s[0:2])
    if s[8:10] == 'PM' and int_hr < 12:
        int_hr += 12
    if s[8:10] == 'AM' and int_hr == 12:
        int_hr -= 12
    if int_hr < 10:
        updated_hr = '0'+ str(int_hr)
    else:
        updated_hr = str(int_hr)
    
    for i in s[2:8]:
        updated_hr = updated_hr + i
    return updated_hr


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result)

    f.close()
