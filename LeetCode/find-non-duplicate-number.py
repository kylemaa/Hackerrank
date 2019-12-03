# https://leetcode.com/problems/single-number/
class Solution:
    # with n being the length of nums and m being the length of dictionary 
    # this solution has the time complexity of O(n + m) which is linear time O(n)
    def singleNumber(self, nums):
        occurrence = {}
        for n in nums:
            try:
                occurrence[n] += 1 
            except KeyError:
                occurrence[n] = 1
        # use .items() to iterating 
        for k, v in occurrence.items():
            if v == 1: 
                return k
            

    # to improve the space complexity we can use XOR op to cancle out the duplicates
    def singleNumber2(self, nums):
        unique = 0 
        for n in nums:
            unique ^= n
            print(unique)
        return unique


print(Solution().singleNumber2([4, 3, 2, 4, 1, 3, 2]))
