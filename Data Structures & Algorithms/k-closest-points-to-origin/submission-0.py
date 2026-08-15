import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []

        for point in points:
            dis = self.getDist(point)
            heapq.heappush(heap, (-dis, point))
            if len(heap) > k:
                heapq.heappop(heap)

        return [item[1] for item in heap]

    def getDist(self, point):
        return math.sqrt((point[0] * point[0]) + (point[1] * point[1]))

        