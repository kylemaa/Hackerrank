def sortNums(nums):
    count = {}
    for n in nums:
        # get a value for the given key if not default to 0
        count[n] = count.get(n, 0) + 1
    return ([999]* count.get(1,0) + [2]* count.get(2,0) + [3]* count.get(3,0))


print(sortNums ([3, 3, 2, 1, 3, 2, 1, 1]))