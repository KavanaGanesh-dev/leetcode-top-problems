# https://leetcode.com/problems/find-peak-element/description/
'''A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.
Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

Constraints:
1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.'''

# some understandings about the question
# I need to find an algorithm that works in O(logn) - that means - i need to find to use binary search algorithm
# But binary search can be used for sorted array - can i use that logic here - yes definitely
# the whole idea is - i am not finding the value; i just need to know which direction to go and return the index

# Here it is : how it works:
# 1.keep 2 pointers left=0 and right=len(nums)-1
# 2.find the mid. keep comparing 
# 3. nums[mid+1] > nums[mid]
    # 4.left = mid+1 ( i skip it here - because i am going up)
# else:
    # right = mid (mid could be the peak)
# finally return the left

# Complexity Analysis:
# Time: O(logn/2) = O(logn) + O(log2) = O(logn) + 1 = O(logn)
# Space: The space complexity is O(1)

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left,right = 0, len(nums)-1

        while left < right:
            mid = (left+right)//2
            if nums[mid+1] > nums[mid]:
                left = mid+1
            else:
                right = mid
        return left
    
nums = [1,2,1,3,5,6,4]
print(Solution().findPeakElement(nums))