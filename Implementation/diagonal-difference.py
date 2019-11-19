# https://www.hackerrank.com/challenges/diagonal-difference/problem
import os

def diagonalDifference(arr):
    # Write your code here
    # Complete this function  
    sum1 = sum2 = 0 
    for i in range(len(arr)):
         sum1 += int(arr[i][i]) # arr[row][column]
         sum2 += int(arr[i][n-i-1])
    return abs(sum1-sum2)

if __name__ == '__main__':
    fptr = open(os.environ['Users/KKyle'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()