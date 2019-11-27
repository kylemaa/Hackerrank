def twoSumBrute(arr, target):
    # Using nested iterative loop to match each element with one another
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]
def twoSumHash(arr, target):
    #table = {i:v for i, v in enumerate(arr)}
    table = {}
    for i, v in enumerate(arr):
        table[v] = i
        complement = target - v 
        if complement in table:
            return [i, table[complement]]

    
target = 5
arr = [1, 4, 5, 6]
print ('brute:', twoSumBrute(arr,target))
print ('hash:', twoSumHash(arr,target))