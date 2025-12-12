'''Problem: top_k frquent elements
https://leetcode.com/problems/top-k-frequent-elements/description/
Approach: use Dict Counter and print the most common K elements using list comprehension
Note : Order of printing in the list can vary
Time complexity: O(nlogk) - O(n) for iterating dictionary and log(k) to print the most k elements which uses heapify/quict sort algorithm
Space complexity: o(n) - for storing in hashmap
'''

from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [integer for integer, freq in count.most_common(k)]
    

nums = [1,2,2,3,3,3]
k = 2
print(Solution().topKFrequent(nums,k))