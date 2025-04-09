class Solution:
    def hammingWeight(self, n:int) -> int:
        '''
        input: 15 (decimal)
        
        sum=1
        n=1111
        n-1=1110
        n&n-1=1110

        sum=2
        n=1110
        n-1=1101
        n&n-1=1100

        sum=3
        n=1100
        n-1=1011
        n&n-1=1000

        sum=4
        n=1000
        n-1=0111
        n&n-1=0000
        '''
        sum = 0
        while n != 0:
            sum += 1
            n &= n -1
        return sum
