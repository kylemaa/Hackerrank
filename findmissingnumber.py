# Given an array A of N integers, return that smallest positive integer that does not occur in A. 
def solution(A):
    A = sorted(A)
    smallest = 0
    for i in range(len(A)):
        if A[i] >= 0 and A[i] != A[i+1] and A[i] != A[i+1] + 1: 
            smallest = A[i]+1
            break
        else:
            return A[-1]+1
    return smallest