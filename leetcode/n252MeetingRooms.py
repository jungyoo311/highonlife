from typing import List
class Solution:
    def canAttendMeetigs(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals) -1):
            if intervals[i][0] > intervals[i + 1][1]:
                return False
        return True
