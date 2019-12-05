def productExceptSelf(nums):
    res = [1] * len(nums) 
    for i in range(1, len(nums)):
        res[i] = res[i-1]* nums[i-1]
    # starting multiplier, right, when iterating backwards 
    right = 1 
    for i in range(len(nums)-2,-1,-1):
        right = right * nums[i+1]
        # since res has the multiplier of the left except self
        # and right has the multipler of the right except self
        # the self will not be accounted for
        res[i] = res[i] * right
    return res