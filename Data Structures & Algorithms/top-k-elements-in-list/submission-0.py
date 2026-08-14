import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # can be done using heap
        freq_count = dict()

        for num in nums:
            freq_count[num] = 1 + freq_count.get(num, 0)
        
        # convert this map to a list of tuple (freq, num)
        # negate to conver to max-heap
        freq_list = [ (-freq, num) for num, freq in freq_count.items()]

        heapq.heapify(freq_list)

        return [heapq.heappop(freq_list)[1] for _ in range(k)]
