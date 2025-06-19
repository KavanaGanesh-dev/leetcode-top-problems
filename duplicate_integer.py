'''python
"""
Problem: duplicate number (finding the only duplicate number)
Link: https://leetcode.com/problems/find-the-duplicate-number/
Approach: Floyd's Tortoise and Hare (cycle detection problem) - effective for extra space and has exactly one duplicate. For multiple duplicates use set approach
Prerequisite: Space: O(1) - inspace movements
Time: = O(n)(for intersection slow moves one step, fast moves by 2 steps) + O(n)(entrance of the cycle) = O(n)
'''

"""Flyod's Totoise problem states that:
1. Find the intersection point 
2. Find the entrance to the cycle = return is the start of the point
"""

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

                
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow



nums = [1,3,4,2,2]
print(Solution().findDuplicate(nums))
        
