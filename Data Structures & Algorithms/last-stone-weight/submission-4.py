import heapq
from collections import deque

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        stones = deque(stones)
        j=0

        while len(stones) >= 2:
            print(f"iteration: {j}, stones: {stones}")
            for i in range(0, len(stones)):
                print(f"inner loop iteration: {i}")
                stone = stones.popleft()
                heapq.heappush(heap, stone)
                print(f"\tpushed {stone} onto heap: {heap}\n\tstones:{stones}")
                if len(heap) > 2:
                    stone2 = heapq.heappop(heap)
                    print(f"\theap too long, popped {stone2}")
                    stones.append(stone2)
                    print(f"\tnew stones: {stones}")
            print(f"heap: {heap}, stones: {stones}")
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            print(f"x: {x}, y: {y}")
            if x > y:
                x = x - y
                print(f"x was larger, appending remainder: {x}")
                stones.append(x)
            elif y > x:
                y = y - x
                print(f"y was larger, appending remainder: {y}")
                stones.append(y)
            else:
                print(f"x and y equal, discarding both")
            j+=1
            print(f"end of iteration, heap: {heap}, stones: {stones}\n")

        if stones:
            return stones[-1]
        else:
            return 0