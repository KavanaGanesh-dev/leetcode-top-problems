'''DESCRIPTION
Design a data structure MovingAverage that efficiently calculates the moving average of the last k numbers from a continuous stream. Each time a new value arrives via next(val), the structure should return the average of the most recent k values (or fewer if less than k values have been received). For example, with k=3, after receiving values [1, 10, 3, 5], calling next(5) should return 6.0 (average of 3, 5, 5).

Input:

MovingAverage(3)
next(1) → 1.0
next(10) → 5.5
next(3) → 4.666...
next(5) → 6.0
Output:

1.0, 5.5, 4.666..., 6.0

Explanation: Window size is 3. First call has only [1], second has [1,10], third has [1,10,3], fourth has [10,3,5] (oldest value 1 is removed).

Constraints:

Window size k is fixed at initialization and 1 ≤ k ≤ 10^4
At most 10^4 calls to next(val) will be made
Values are in range [-10^5, 10^5]
Must achieve O(1) time complexity for next() operation
Must use O(k) space complexity'''

# Insights from question:
# array = [], sum = 0, window_size = k = 3
# 1st iteration: next(1)->array = [1], sum = 1, avg = 1/1 = 1.0
# 2nd iteration: next(10) ->array = [1,10], sum =11, avg = 11/2 = 5.5
# 3rd iteration: next(3) ->array = [1,10,3], sum = 14, avg = 14/3 = 4.66
# 4th iteration: next(5) ->array = [1,10,3,5], sum = 19, however length of array > k, pop here to maintain k size, sum=sum-popelement, avg = 18/3 = 6.0
# I am going to choose dque here: bcos of its simltaneously adding deleting feature - this gives benefits of O(1) - pop opertaion in the queue


from collections import deque
class Movingavg:


    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.sum = 0


    def valnext(self, val):
        self.queue.append(val)
        self.sum = self.sum + val
        

        if len(self.queue) > self.size:
            pop_ele = self.queue.popleft()
            self.sum = self.sum - pop_ele

        return self.sum / len(self.queue)



ma = Movingavg(3)
print(ma.valnext(1))
print(ma.valnext(10))
print(ma.valnext(3))
print(ma.valnext(5))
