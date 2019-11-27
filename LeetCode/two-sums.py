def twoSumBrute(arr, target):
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if arr[i] + arr[j] == target:
                return [arr[i], arr[j]]


target = 5
arr = [1, 4, 5, 6]
print(twoSumBrute(arr,target))