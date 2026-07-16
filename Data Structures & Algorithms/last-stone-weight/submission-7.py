import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        print(f"heap: {heap}")

        while len(heap) >= 2:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if x < y:
                x = x - y
                heapq.heappush(heap, x)
            elif x > y:
                y = y - x
                heapq.heappush(heap, y)
                
        if heap:
            return abs(heap[0])
        else:
            return 0