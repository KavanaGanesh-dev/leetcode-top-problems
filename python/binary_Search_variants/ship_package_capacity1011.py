'''A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
Example 2:
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
Example 3:
Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
Constraints:
1 <= days <= weights.length <= 5 * 104
1 <= weights[i] <= 500'''

# Rephrasing the question:
# I need to find the minimum capacity that i can load the packages to the conveyor belt, 
    # packages should be sent in order -  clue -  packages weight is already sorted
    # packages sent to conveyor belt - should not exceed the number of days given
    # packages weights should not exceed the minimum capacity which should not exceed the number of days to do the work


# Idea:
# 1. The minimum capacity coulbe be - one option -  the maximum number of weights
# 2. The max capacity can be the - sum of the total numbers of weight
# 3. The minimum capacity will lie between the max number of weight - sum (total numbers of weight)
# how to find the number that lies between that - binary search, left - max number in the weight, right - sum of the weights. fidn the mid

# complexity
# Time : binary search operation - so the number iteration is reduced = log(sum(weight)) + canship method for each weight(n)
    # total = n * log(sum(weight))
# Space :O(1) just variables and other math operations
from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) //  2
            capacity = mid
            if self.capacityship(capacity, weights, days) is True:
                right = mid
            else:
                left = mid+1
        return left

    
    def capacityship(self, capacity, weights, days):
        current_load = 0
        job_days = 1
        for weight in weights:
            
            if weight > capacity:
                return False
            
            if current_load + weight <= capacity:
                current_load = current_load + weight
            else:
                job_days =  job_days + 1
                current_load = weight

        return job_days <= days




weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(Solution().shipWithinDays(weights, days))