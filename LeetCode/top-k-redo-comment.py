import collections
import heapq
def topKFrequent(self, nums, k):
    # Dictionary that has count for each of the element in nums.
    count = collections.defaultdict()
    for n in nums:
        count[n] += 1
    # Push the values with the key n into a heap, in ascending order of value.
    heap = []
    for key, value in count.items():
        heapq.heappush(heap,(value,key))
        if len(heap)>k:
            heapq.heappop(heap)
    # Push the remaining k most freqent numbers into res stack by popping them off. 
    res = []
    while len(heap)>0: 
        res.append(heapq.heappop(heap))
    return res

    