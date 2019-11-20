# Given an array A of N integers, return that smallest positive integer that does not occur in A. 
import os
def solution(arr):
    a = sorted(arr)
    print(a)
    smallest = 0
    for i in range(len(A)-1):
        if A[i] > 0:
            if A[i] != A[i+1] and A[i]+1 != A[i+1]: 
                smallest = A[i]+1
                return smallest 
            # I can check this at the beginning. 
            else:
                return A[-1]+1


A = [1, 2, 6, 4]
print(solution(A))
