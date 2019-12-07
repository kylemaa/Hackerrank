import heapq
import random

def findKthLargest_brute(nums,k):
    return sorted(nums)[len(nums)-k]

def findKthLargest_heap(nums, k):
    return heapq.nlargest(k, nums)[-1]

def findKthLargest_partition(nums,k):
    def select(list, l, r, index):
        if l == r:
            return list[l]
        pivot_index = random.randint(l, r)
        # swap the pivot to the beginning of the list
        list[l], list[pivot_index] = list[pivot_index], list[l]
        i = l
        for j in range(l + 1, r + 1):
            if list[j] < list[l]:
                i += 1
                list[i], list[j] = list[j], list[i]
    # move pivot to the correct location
        list[i], list[l] = list[l], list[i]
    # recursively partition one side
        if index == i:
            return list[i]
        elif index < i:
            return select(list, l, i - 1, index)
        else:
            return select(list, i + 1, r, index)
    return select(nums, 0, len(nums) - 1, len(nums) - k)




print(findKthLargest_partition([3, 5, 2, 4, 6, 8], 3))