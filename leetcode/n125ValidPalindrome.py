class Solution:
    def isPalindrome(self, s:str) -> bool:
        # in-processing takes less space complexity 
        # more efficient
        '''
        Test case 0: "A man, a plan, a canal: Panama"
        '''
        left, right = 0, len(s) -1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True