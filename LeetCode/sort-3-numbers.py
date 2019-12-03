# linear time with O(n + m), n be the size of nums and m be the size of dictionary
def sortNums(nums):
    count = {}
    for n in nums:
        # get a value for the given key if not default to 0
        count[n] = count.get(n, 0) + 1
    return ([999]* count.get(1,0) + [2]* count.get(2,0) + [3]* count.get(3,0))

# linear time with O(n), in this algorithm brute force swapping the known elements.
def sortNums2(nums):
    start = 0 
    end = len(nums) -1 
    index = 0 
    while index <= end:
        if nums[index] == 1:
            # swap
            nums[index], nums[start]= nums[start], nums[index]
            start += 1 
            index += 1
        elif nums[index] == 2:
            # do nothing
            index += 1
        elif nums[index] == 3:
            # swap
            nums[index], nums[end]= nums[end], nums[index]
            end -= 1 
    return nums

print(sortNums2([3, 3, 2, 1, 3, 2, 1, 1]))