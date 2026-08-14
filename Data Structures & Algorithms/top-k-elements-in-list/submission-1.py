import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # can be done using heap
        freq_count = dict()

        for num in nums:
            freq_count[num] = 1 + freq_count.get(num, 0)
        
        heap = []
        for num, freq in freq_count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [heapq.heappop(heap)[1] for _ in range(k)]
