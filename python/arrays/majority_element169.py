# https://leetcode.com/problems/majority-element/description/
'''Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array 
Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
The input is generated such that a majority element will exist in the array.
Follow-up: Could you solve the problem in linear time and in O(1) space?'''

# some insights after understanding the problem
# Given an array with integers - i need to return the most common integer present
# Solution Methods:
# 1.Methods: create the hashmap wiht number and frequency
# then use the built in method Counter(arr).most_common(1)[0][0] - this gives the max frequent number
# But the compexity here is O(n) space 

# Method 2: focus on saving the space:
# 1.I initialize the counter = 0, my candiidate is initally None
# 2. check to see my counter == 0, then i assign the candidate with num value
    # 3. when i encounter the same candidate: increment the counter
    # 4. when i encounter the differnt candidate: decrement the counter
# 5. Finally return the candidate
# Analysing the complexity:
# Time : O(n) - I traverse through all the element to play with the number
# Space: O(1) - I used counter, candidate variable, nothing much i saved - so it should be O(1)

from typing import List

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        candidate = None

        for num in nums:
            if counter == 0:
                candidate = num
            if num == candidate:
                counter = counter+1
            else:
                counter = counter-1
        return candidate
    
nums = [2,2,1,1,1,2,2]
print(Solution().majorityElement(nums))
