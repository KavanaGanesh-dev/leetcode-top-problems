'''Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 
Constraints:
1 <= k <= points.length <= 104
-104 <= xi, yi <= 104'''

# Some insights from the problem
# 1.Remember - square root(x2-x)^2 + (y2-y1)^2 = square root(x2^2 + y2^2) - because x1, y1 = (0,0)
# 2.squareroot is monotonically increasing function - so ignore square root , the equation become distance^2 = (x2^2+y2^2)
# 3. so basicallly maintain the length of list/array with k and check for distance^2 - but list/array 
# 4. List/array is bad- appending and popping is expensive
# 5. lets use heap - max or min? max stores largest, min stores smallest - choice - max heap is best - O(nlogk) - log k comes from push or pop operations
# 6. if i did sortig - bad choice - o(nlogn)

'''1. Create empty max_heap
2. For each point in points:
   - Calculate distance²
   - If heap size < k:
       append the current element
   - Else (heap is full):
       if current distance^2  < rootdistance^2 (root is large)
            pop the root
            append the current_distance element
        else:
            dont do anything
3. Return the k points from heap'''

# Complexity analysis:
# 1. Time -  we are iterating for each element in nestedlist - o(n)
    # but the operations of the heap-add and remove(o(logk)) - you are doing for the size of the heap-which is k
    # Overall time - O(nlogk)
# 2.Space - We are using heap - to store elemenst for length of k - o(k)


from typing import List
import heapq 
# by defualt python's heapq is the min heap. To make it max heap - i will negate it

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for x, y in points:
            distance = x**2 + y**2

            if len(min_heap) < k:
                heapq.heappush(min_heap,(-distance,[x,y])) #(-10, [1,3])
            else:
                root_distance = -min_heap[0][0] #10 - gives this value
                if distance < root_distance:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap,(-distance,[x,y])) 
                else:
                    continue

        return [distance for distance, point in min_heap]
    

points = [[3,3],[5,-1],[-2,4]]
k = 2
print(Solution().kClosest(points,k))

'''**Heap visualization:**
```
Before pop:                After pop:              After push:
   -26,[5,-1](root)              -18,[3,3] (root)           -20,[-2,4](root)
       /                                               /
-18,[3,3]                                        -18,[3,3]'''