class Solution:
    def checkPossibility(self, nums):
        # egde case
        if len(nums)< 2:
            return False 
        dips = 0 
        prev_num = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                dips -= 1 
                prev_num = nums[i]
    
            elif nums[i] < nums[i+1]:
                dips += 1

            if prev_num > nums[i+1] and dips < 0:
                return False
        
        if dips > -2:
            return True 
        else: 
            False

print(Solution().checkPossibility([4,2,6]))