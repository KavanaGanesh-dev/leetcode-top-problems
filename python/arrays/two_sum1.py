'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
from typing import List'''

# Analysing the question
# Given question: list of numbers, target. return the indices of two numbers in a list that sum upto target
# a+b = target: b = target-a, a is the value 
# use dict to store key and value pair . key each number given in the list: value is the index
# find complement b = target-value
# chek for complement - does complement lies in the dictionary
# if yes, then return the index of the both number that sum upto target
# if no then create the dictionary to store the key value pair

# complexity analysis
# Time: We are looping through the method onece - O(n)
# Space: Dictionary to store the key:value pairs - O(n)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = dict()
        
        for index, value in enumerate(nums):
            b = target-value
            if b in new_dict:
                return [new_dict[b], index]
            new_dict[value] = index
            

# nums = [2,7,11,15], target = 9
nums = [0,-1,2,-3,1]
target = -2
print(Solution().twoSum(nums, target))
