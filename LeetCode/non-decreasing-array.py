class Solution:
    def checkPossibility(self, nums):
        # egde case
        if len(nums)< 2:
            return False 
        dips = None
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if dips is not None:
                    dips = i
        # if there's no dip
        if dips is None:
            return True
        if dips == 0: 
            return True
        if dips == len(nums) -2:
            return True 
        if nums[dips] <= nums[dips + 2] or nums[dips - 1] <= nums[dips + 1]:
            return True
        return False

        
        
        
print(Solution().checkPossibility([4,2,6]))