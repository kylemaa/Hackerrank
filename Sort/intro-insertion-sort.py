# https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    # find the value of the last array element
    value = arr[-1]
    # find the starting iteration point, next to the last value
    i = arr[n-2]
    while (value < arr[i]) and (i >=0):
        arr[i+1] = arr[i]
        print(''.join(map(str,arr)))
        i -= 1 
    arr[i+1] = value
    print(''.join(map(str,arr)))