from typing import List
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # use min-heap to keep track of free rooms
        free_rooms = []
        intervals.sort(key=lambda x: x[0])
        # Add the first meeting's end time
        heapq.heappush(intervals[0][1])
        return 0
    