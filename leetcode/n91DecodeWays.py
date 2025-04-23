class Solution:
    class Solution:
        def numDecodings(self, s: str) -> int:
            '''
            can decode 1 digit at a time (if it's not 0)
            can decode 2-digits at a time (if the number is between 10 and 26)

            Dynamic Programming solution using bottom-up approach
            
            dp[i] = number of ways to decode substring s[i:]
            final answer will be stored in dp[0]


            '''

            dp = {len(s) : 1}
            for i in range(len(s) -1, -1, -1):
                if s[i] == "0":
                    dp[i] = 0
                else:
                    dp[i] = dp[i + 1]
                if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                    dp[i] += dp[i + 2]
            return dp[0]



        