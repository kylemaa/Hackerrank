def sortNums(nums):
    count = {}
    for n in nums:
        # get a value for the given key if not default to 0
        count[n] = count.get(n, 0) + 1
    return ([999]* count.get(1,0) + [2]* count.get(2,0) + [3]* count.get(3,0))

def sortNums2(nums):
    start = 0 
    end = len(nums)
    index = 0 
    while index <= end:
        if nums[index] == 1:
            # swap
            start += 1 
            index += 1
        if nums[index] == 2:
            # do nothing
        if nums[index] == 3:
            # swap

print(sortNums ([3, 3, 2, 1, 3, 2, 1, 1]))