from heapq import heappush, heappop
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Step 1: Create a min-heap
        min_heap = []

        # Step 2: Calculate distances and add to the heap
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)  # Calculate distance to origin
            heappush(min_heap, (dist, [x, y]))  # Push distance and the point as a tuple

        # Step 3: Extract the closest k points
        result = []
        for _ in range(k):
            result.append(heappop(min_heap)[1])  # Extract k points from the heap

        return result
