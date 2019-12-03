# Helper function because we are going use recursion
class Solution:
    def permute(self,nums):
        # returning all possible sets by appending them to res 
        res = []
        def permuteHelper(start, end):
            if start == end:
                res.append(nums)
            for i in range(start, len(nums)):
                #swap for permutations
                nums[start], nums[i] = nums[i], nums[start]
                permuteHelper(start +1, len(nums))
                #back track the nums array to init state
                nums[start], nums[i] = nums[i], nums[start]
        permuteHelper(0,len(nums))
        return res


arr = [1,2,3]
print(Solution().permute(arr))