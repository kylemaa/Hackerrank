def threesum(nums):
    nums.sort()
    res = []
    # set up 3 some with fixed index
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # two sum def of the sub array in nums
        # pointers at the beginning and the end of of nums
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                res.append(nums[i], nums[j], nums[k])
                while j < k and nums[j] == nums[j+1]:
                    j += 1
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
                j += 1
                k -= 1
            elif nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            else:
                j += 1
        return res


nums = [-1, 0, 1, 2, -1, -4]
print(threesum(nums))
