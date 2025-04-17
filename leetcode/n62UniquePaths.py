class Solution:
    def uniquePaths(self, m:int, n:int) -> int:
        '''
        rather than using (col,row), (i,j) use directions in the matrix problem for preventing confusions
        '''
        dp = [[1] * n for _ in range(m)]
        for down in range(1, m):
            for right in range(1, n):
                dp[down][right] = dp[down -1][right] + dp[down][right-1]
        return dp[m-1][n-1]