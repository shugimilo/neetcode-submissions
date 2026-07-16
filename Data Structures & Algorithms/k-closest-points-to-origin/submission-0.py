import heapq
import math

class Solution:
    def calculateDistance(self, point: List[int]) -> float:
        return math.sqrt(point[0]**2 + point[1]**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [-self.calculateDistance(point) for point in points]
        print(distances)

        heapq.heapify(distances)

        print(distances)

        while len(distances) > k:
            heapq.heappop(distances)

        res = []

        for point in points:
            if -self.calculateDistance(point) in distances:
                res.append(point)

        return res
