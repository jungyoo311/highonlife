class Solution:
    def countBits(self, n:int) -> int:
        
        def ret_sum(n):
            sum = 0
            while n != 0:
                sum += 1
                n &= n-1
            return sum
        # make empty list with exact size
        result  = [0] * (n+1)
        for i in range(0,n+1):
            result[i] = ret_sum(i)
        return result