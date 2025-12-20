'''You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums
Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b'''
 

# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# Example 2:

# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
 

# Constraints:
# 0 <= nums.length <= 20
# -231 <= nums[i] <= 231 - 1
# All the values of nums are unique.
# nums is sorted in ascending order.


# Some insights about the problem:
# 1. 2 pointer approach
# 2. need to travel all the way till the length of the array. 
# 3. remember - we check the next elemnt is the sum of the current + 1 . so we might need to track of the last element in the array 



# Complexity analysis:
# 1. Time: we are iterating throught the length of the array: j increments exactly once = O(n)
# 2 Space: we use result to store the range. - O(n)
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i, j = 0,0
        result = []

        while j < len(nums):
            if j+1 < len(nums) and nums[j+1] == nums[j] + 1:
                j = j+1
 
            else:
                if i == j:
                    result.append(str(nums[i]))
                else:
                    result.append(str(nums[i]) + "->" + str(nums[j]))

                j= j+1
                i=j
        return result


nums = [0,1,2,4,5,7]
print(Solution().summaryRanges(nums))