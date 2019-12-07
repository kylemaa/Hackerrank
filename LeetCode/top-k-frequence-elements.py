import collections
class Solution:
    def topKelements(self, nums, k):
        count = collections.defaultdict(int)
        for n in nums:
            count[n] += 1
        heap = []
        for key, v in count.items():
            heapq.heappush(heap, (v,key))
            if len(heap) > k:
                heapq.heappop(heap)      
        res = []
        while len(heap) > k:
            res.append(heapq.heappop(heap)[1])
        return res

    