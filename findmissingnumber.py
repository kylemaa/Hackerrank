# Given an array A of N integers, return that smallest positive integer that does not occur in A. 
import os
def solution(A):
    for i in range(len(A)-1):
        print(A[i])
        if A[i] >= 0 and A[i] != A[i+1] and A[i] != A[i+1] + 1: 
            smallest = A[i]+1
            return smallest 
        else:
            smallest = A[-1]+1
    return smallest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = []

    for _ in range(n):
        A.append(list(map(int, input().rstrip().split())))
    
    result = solution(A)

    fptr.write(str(result) + '\n')

    fptr.close()
