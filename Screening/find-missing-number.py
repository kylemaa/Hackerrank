# Given an array A of N integers, return that smallest positive integer that does not occur in A. 
import os
def solution(arr):
    m = max(arr)
    if m < 1:
        return 1
    if len(arr)== 1:
        if arr[0] == 1:
            return 2
        else:
            return 1
    l = [0]* m 
    for i in range(len(arr)):
        if arr[i]>0:
            if l[arr[i]] !=1:
                l[arr[i]] = 1
    for j in range(len(l)):
        if l[j] == 0:
            return i+1
    return i+2

A = [1, 2, 5, 4]
print(solution(A))
