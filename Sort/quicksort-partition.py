# https://www.hackerrank.com/challenges/quicksort1/problem

def quickSort(arr):
    right = []
    left = []
    result = []
    middle = arr[0]
    for i in range(1, len(arr)):
        if arr[i]< arr[0]:
            left.append(arr[i])
        elif arr[i] > arr[0]:
            right.append(arr[i])
    for i in left:
        result.append(i)
    result.append(middle)
    for i in right:
        result.append(i)
    return result