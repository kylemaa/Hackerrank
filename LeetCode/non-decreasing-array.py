class Solution:
    def checkPossibility(self, nums):
        # egde case
        if len(nums)< 2:
            return False 
        dips = None
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                # if dips more than once
                if dips is not None:
                    return False
            dips = i
        # if there's no dip
        if dips is None:
            return True
        # if there's one dip at first index
        if dips == 0: 
            return True
        # if there's one dip next to last
        if dips == len(nums) -2:
            return True 
        # if number at that dip smaller than the next two indexes or the other case
        if nums[dips] <= nums[dips + 2] or nums[dips - 1] <= nums[dips + 1]:
            return True
        return False

        
        
        
print(Solution().checkPossibility([4,2,6]))