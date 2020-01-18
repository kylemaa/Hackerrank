# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# Assume nums1 and nums2 cannot be both empty.

import math


def findMedianSortedArrays(nums1, nums2):
    combine = sorted(nums1 + nums2)
    n = len(combine)
    if n % 2 != 0:
        median_index = math.floor(n/2)
        return combine[median_index]
    else:
        mid_point_1 = combine[int(n/2 - 1)]
        mid_point_2 = combine[int(n/2)]
        median = (mid_point_1 + mid_point_2) / 2
        return median


nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))
