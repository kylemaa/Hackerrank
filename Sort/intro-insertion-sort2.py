def insertionSort2(n, arr):
    for i in range (1,n):
        # starting point j is index 0, i is index 1
        key = arr[i] 
        j = i - 1 
        while (arr[j]> key) and j>=0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        