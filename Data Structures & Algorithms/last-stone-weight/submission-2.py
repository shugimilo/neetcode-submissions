import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) >= 2:
            x = stones.pop()
            y = stones.pop()
            if x > y:
                x = x - y
                heapq.heappush(stones, x)
            elif x < y:
                y = y - x
                heapq.heappush(stones, y)
            
        if stones:
            return stones[-1]
        else:
            return 0