class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        def checkPalindrome(l, r):
            # if left, right ptrs are in-bound and they are the same
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    res = s[l : r + 1]
                l -= 1
                r += 1
            
        for i in range(len(s)):
            # odd length palindrome
            checkPalindrome(i,i)
            # even length palindrome
            checkPalindrome(i,i+1)
        return res   