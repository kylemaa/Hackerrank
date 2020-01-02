class Solution:
    # brute force solution with time complexity of O(N*N*N), N being the size of array nums.
    def findPythagoreanTriplets(self, nums):
        for a in nums:
            for b in nums:
                for c in nums:
                    if a*a + b*b == c*c:
                        return True
        return False

    # memoiztion solution with time complexity of O(N*N), N neing the size of the array nums
    def findPythagoreanTriplets2(self, nums):
        squares = set([n*n for n in nums])
        for a in nums:
            for b in nums:
                if a*a + b*b in squares:
                    return True
        return False


print(Solution().findPythagoreanTriplets2([3, 5, 12, 5, 13]))
