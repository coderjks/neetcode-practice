import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)
        print(stones)

        while stones:
            x =  -1 * heapq.heappop(stones)
            if not stones:
                return x
            
            y = -1 * heapq.heappop(stones)

            if x < y:
                heapq.heappush(stones, -(y - x))
            elif x > y:
                heapq.heappush(stones, -(x - y))
        
        return 0