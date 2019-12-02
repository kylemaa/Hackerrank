# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
# Because the array is already sorted, we can use binary search tree for solve for logarithmic time. 
class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
      lo = 0
      hi = len(nums)
      while 

