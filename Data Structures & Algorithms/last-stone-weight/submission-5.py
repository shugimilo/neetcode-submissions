import heapq
from collections import deque

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        stones = deque(stones)
        while len(stones) >= 2:
            for i in range(0, len(stones)):
                stone = stones.popleft()
                heapq.heappush(heap, stone)
                if len(heap) > 2:
                    stone2 = heapq.heappop(heap)
                    stones.append(stone2)
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if x > y:
                x = x - y
                stones.append(x)
            elif y > x:
                y = y - x
                stones.append(y)

        if stones:
            return stones[-1]
        else:
            return 0