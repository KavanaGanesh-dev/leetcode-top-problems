'''You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length'''



# Ingights from this question:
# Bruteforce approach  -traverse and then find max = O(k(n-k)) = O(k)
# Thinling of something better - deque is an option
# Everytime i slide from left to right maintain the window size - so i am removing element from left and adding element from right
# if we store the values in deque its of no use bcos again i have to find the max and in that deque- the operation is again O(k)
# the key trick is to keep-t he maximum element in the deque(where the deque stores the index of the value) -  and remove all the element less than the max value. The max value in the deque is position 0 (left)

# Some core rules to remember to solve this problem
# 1.use double ended que - for O(1) operations like popleft, pop, append
# 2.store indices not values - bcos i want to access the value nums[deque[0]] and to check if elements are still in the window
# 3. deque values should be in decreasing order nums[deque[0]]> nums[deque[1]]>nums[deque[2]]
# 4 remove from front to maintain the window size - 
# remove the lesser values from back

# window size = i-k+1
# window is complete if i>= k-1


# Complexity analysis
# Space cpmplexity: O(k) - bcos we are storing onlu k element in deque
# Time  - O(n) - iterating array once while deque operations is O(1)



from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result= []
        for i in range(len(nums)):
            # A. check front of deque is within/out of the window - ie. remove the indices that are out of the window
            if q and q[0] < i-k+1:
                q.popleft()

            # B. Keep the max value at index 0 and remove all the less values wrt to the max value as its of no use
            while q and nums[q[-1]]<nums[i]:
                q.pop()  
            # C. Append the each element to the deque 
            q.append(i)
            # D. record the max when window is formed
            if i >= k-1: #if k=3, we need to form index of 0,1,2
                result.append(nums[q[0]])

        return result

nums = [1,3,-1,-3,5,3,6,7]
k = 3
# Output: [3,3,5,5,6,7]
print(Solution().maxSlidingWindow(nums,k))