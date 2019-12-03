# https://leetcode.com/problems/single-number/
class Solution:
    # with n being the length of nums and m being the length of dictionary 
    # this solution has the time complexity of O(n + m)
    def singleNumber(self, nums):
        occurrence = {}
        for n in nums:
            try:
                occurrence[n] += 1 
            except KeyError:
                occurrence[n] = 1
        for x in occurrence:
            if occurrence[x] == 1:
                return occurrence[x]


print(Solution().singleNumber([4, 3, 2, 4, 1, 3, 2]))
