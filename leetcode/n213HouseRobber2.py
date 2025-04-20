from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # first house is neighbor of the last one.
        '''
        [1,2,3,1]
        even or odd
        [1,2,3,2,1]
        1       n-1
        <      >
           <     >
           2    n
        '''
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        def checkMax(houses):
            h = len(houses)
            dp = [0] * h
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            for i in range(2, h):
                dp[i] = max(houses[i] + dp[i-2], dp[i-1])
            return dp[-1]
        return max(
            checkMax(nums[:-1]), #exclude last
            checkMax(nums[1:]) # exclude first
        )