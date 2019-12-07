import collections
import heapq

class Solution:
    def topKelements(self, nums, k):
        count = collections.defaultdict(int)
        for n in nums:
            count[n] += 1
        heap = []
        for key, v in count.items():
            # heap push method
            heapq.heappush(heap, (v,key))
            if len(heap) > k:
                # heap pop the ones that most frequent based on the value v (pop the smallest/ min-heap)
                heapq.heappop(heap)      
        res = []
        while len(heap) > 0:
            res.append(heapq.heappop(heap)[1])
        return res

print(Solution().topKelements([3, 3, 1, 1, 2, 5, 7, 8], 2 ))
    