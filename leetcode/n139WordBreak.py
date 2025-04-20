from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP will store T/F if the index starts with prefix string is in the wordDict
        # base-case: dp[len(s)] == True; if it reaches the last + 1 index then it automatically
        # proved that result is true

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        # Bottom-up Approach
        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                # boundary check first; do we have enough words to check?
                if (i + len(w) <= len(s)) and s[i:i+len(w)] == w:
                    dp[i] == dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]