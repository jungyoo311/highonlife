from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        [1,2,3,1]
        [r1, r2, n, n+1 ...]
        
        '''
        # SOL 1 neetcode way
        # r1, r2 = 0,0
        # for num in nums:
        #     # for the val in position n
        #     temp = max(r1 + num, r2)
        #     # for the position n+1, update r1, r2 respectively.
        #     r1 = r2
        #     r2 = temp
        # return r2

        
        # SOL 2, using DP
        n = len(nums)
        dp = [-1] * n
        if n == 1:
            return nums[0]
        dp[0], dp[1] = nums[0], nums[1]
        # [1,2,3,1]
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]
