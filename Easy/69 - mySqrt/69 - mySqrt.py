class Solution:
    def mySqrt(self, x: int) -> int:
        if (x<0) or (2**31 -1 <x):
            return -1
        if x==0:
            return 0
        if x==1:
            return 1
        left, right=0, x
        while left<=right:
            median=(left+right)//2
            if median*median==x:
                return median
            elif median*median <x:
                left=median+1
            else: 
                right=median -1 
        return right