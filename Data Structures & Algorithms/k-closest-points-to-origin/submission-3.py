import heapq
from math import sqrt

class Solution:
    def calculateDistance(self, point: List[int]) -> float:
        return sqrt(point[0]**2 + point[1]**2)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            heapq.heappush(heap, (-self.calculateDistance(point), point))
            if len(heap) > k:
                heapq.heappop(heap)

        return [point[1] for point in heap]