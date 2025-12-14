'''Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104'''
# https://leetcode.com/problems/merge-intervals/

# Insights from understanding this problem
# 1. Its a nested list (Rememebr - list is not sorted) -  i need to sort that first
# 2. There can be 2 options: lists can overlap and non-overlap.
# 3. When overlap - i should see how to put the merge interval
# 4. when they dont overlap - how to deal with the output


# Complexity analysis:
# Time -  sorting is O(nlogn), Looping is O(n). So therefore - taking the highest - O(nlogn)
# space - Nested list means its not n^2(this assumption is wrong)lets breakdown
# There are n inputs and each inout has 2 datapoints. so 2(times)n. ignore constant. - O(n)

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])

        return result
    

intervals = [[1,3],[2,6],[8,10],[15,18]]    
print(Solution().merge(intervals))