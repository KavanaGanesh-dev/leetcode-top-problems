# https://leetcode.com/problems/squares-of-a-sorted-array/description/
'''Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 
Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?'''

# Some insights from understanding the problem
# solution1: pick each number traverse through the list- find the square and sort it and return
# drawback: O(n) for traversing and sorted - O(logn). total = O(nlogn)
# solution2: lets solve using two pointer approach
# 1. keep right pointer from len(arr)-1
# 2. keep left pointer from 0
# 3. initate the array of size of nums
# 4. keep a location ptr - this is needed to put the value at the corresponding location for arr created
    # (location ptr value start from len(nums)-1)
# 5. iterate through loop left becomes eual to the right
# 6. check for condition square on the right ptr value is greater than the sqaure left ptr value
    # 7. put the value in the array - to the location ptr 
    # 8. then decrement the right ptr value
# 9. else:
    # 10. put the value in the array - to the location ptr 
    # 11. increment the valeu of the left pointer
# 12.keep decrementing the value of the location pointer
# 13. finally return the arr


# Complexity:
# Time: single pass from 2 pointer approach - O(n)
# Space: I have used arr with the size of nums - O(n) - to store the elments


from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        loc = len(nums)-1
        arr = [0]* len(nums)

        while left <= right:
            if nums[right] * nums[right] > nums[left] * nums[left]:
                arr[loc] = nums[right] * nums[right]
                right = right-1
            else:
                arr[loc] = nums[left] * nums[left]
                left = left+1
            loc = loc-1
        return arr
    
nums = [-7,-3,2,3,11]
print(Solution().sortedSquares(nums))

