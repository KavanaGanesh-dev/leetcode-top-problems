'''Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)'''

# Some insights to understand
# if i iterate through each element and do the brute force - will have to use floor division- against the problem constraint
# I will create 2 array - left and right array -  finally do the array multiplication 

# Time complexity
# Space = o(n). creating 3 arrays left, right, answer. however- 3(O(n)) = O(n)
# Time = We are looping through each arrays at once. So its 3O(n) = O(n)

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        left[0] = nums[0]
        for i in range(1, len(nums), 1):
            left[i] = left[i-1] * nums[i-1]
        

        right = [0] * len(nums)
        right[len(nums)-1] = 1
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
            

        answer = [0] * len(nums)
        for i in range(0, len(nums), 1):
            answer[i] = left[i] * right[i]

        return answer
    

nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))