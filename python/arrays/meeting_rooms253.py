'''Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000'''



# Definition of Interval:

from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        start = []
        end = []

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)

        start.sort()
        end.sort()

        i, j = 0, 0
        rooms = 0
        max_rooms = 0

        while i < len(start):
            if start[i] < end[j]:
                rooms += 1
                max_rooms = max(rooms, max_rooms)
                i += 1
            else:
                rooms -= 1
                j += 1
        return max_rooms
    

intervals = [Interval(0, 30),Interval(5, 10),Interval(15, 20)]
print(Solution().minMeetingRooms(intervals))