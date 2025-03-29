from typing import List
class Solution:
    def maxArea(self, height: List[int])-> int:
        '''
        max Area:
        1. largest width
        2. largest height
        '''
        #1 this prints out ascending sorted list
        # does not modify the original height
        # print(sorted(height))
        # 2 this is printing out None in-place sorting
        # build a map include all indexes and values
        # two ptr approach.
        maxArea = 0
        left = 0
        right = len(height) -1
        while left < right:
            width = right - left
            maxArea = max(maxArea, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
