"""This function calls a helper function to recurse on each iteration of the given array for its permutation"""


class Solution:
    def permute(self, nums):
        res = []

        def permuteHelper(start, end):
            # Whenever the start reaches the end of the array, append a copy of the array
            if start == end:
                res.append(nums.copy())
            for i in range(start, len(nums)):
                # swap for permutations
                nums[start], nums[i] = nums[i], nums[start]
                permuteHelper(start + 1, len(nums))
                # back track the nums array to initial state
                nums[start], nums[i] = nums[i], nums[start]

        permuteHelper(0, len(nums)-1)
        return res


arr = [1, 2, 3]
# Should print [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
print(Solution().permute(arr))
