# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers pointing at the end and beginning
        # of array height
        j = len(height) - 1
        i = 0
        max_area = 0
        # closing in from both sides of the array height
        while i < j:
            if height[i] < height[j]:
                current_area = height[i] * abs(j-i)
                i += 1
            else:
                current_area = height[j] * abs(j-i)
                j -= 1
            if max_area < current_area:
                max_area = current_area
        return max_area
