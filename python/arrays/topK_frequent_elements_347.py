'''Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

 

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size'''

# Insights from question:
# 1. we need to track the count /frquency of each number and finally prin the result in a list
# 2. I need to create a dictionary - store key-value pairs
# 3. sort, and finally return the max number wrtk 
# THIS COMPLEXITY IS O(nlogn) - I DONT WANT

# Better solution
# 1. we need to track the count /frquency of each number and finally prin the result in a list
# 2. I need to create a dictionary - store key-value pairs
# 3. create a bucket for each number wih index and frequnecy therfore bucket = [[], [],[],[],[],[],[],[]]
# 4. Then try to append the value(freq) to weights - [[],[3]],[2],[1],[], [], [],[]
                                    # index:          0,  1,   2,  3, 4,  ,5,  6, 7,
# 5. now travrese form behinf of the weights and keep appending untill the length of result is k
# 6. print the result


# Analysing complexity:
# Time: iterate throught dict - O(n)
    # iterate form the behind of weights - O(n) = notO(n2) why? - we are iterating once for each unique element within the inner loop
    # TOTAL = O(N)

# space: created a dictionary, created a bucket, created a result = Each operation is O(n) (Remember if its an N*N dimension -  then its)
    # TOTAL = O(N)

from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count becomes: {1: 3, 2: 2, 3: 1}
        count = Counter(nums)

    # let me create the weights
        weights = [[] for _ in range(len(nums)+1)]

        for key, value in count.items():
            weights[value].append(key)

        result = []
        for i in range((len(weights)-1), 0, -1):
            for n in weights[i]:
                result.append(n)
                if len(result) == k:
                    return result  
        return result
    

nums = [1,2,1,2,1,2,3,1,3,2]
k = 2 
# nums = [1,1,1,2,2,3]
# k = 2
print(Solution().topKFrequent(nums, k))