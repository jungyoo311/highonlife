class Solution:
    def countSubstrings(self, s:str) -> int:
        cnt = 0
        def checkPalindrome(l,r):
            nonlocal cnt
            # while it's in-bound and it's palindrome, increment cnt and change the boundaries
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l += 1
                r -= 1
        for i in range(len(s)):
            checkPalindrome(i,i) # odd length
            checkPalindrome(i,i+1) # even length
        return cnt