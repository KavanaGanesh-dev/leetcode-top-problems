'''Problem: two sum
https://leetcode.com/problems/two-sum/description/
Approach: Hashmap - check if complement exist in the map otherwise update hashmap with new value and index as key-value pair
Prerequesite: Return the answer with smaller index first
Time complexity:
Space complexity:
'''

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = dict()
        
        for index, value in enumerate(nums):
            b = target-value
            if b in new_dict:
                return [new_dict[b], index]
            new_dict[value] = index
            

nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))
