class Solution(object):
    def reverse(self, x):
        num = abs(x)
        res = 0
        sign = -1 if x < 0 else 1 
     
        while num > 0:
            ld = num % 10
            res = (res*10)+ld
            num//=10
        res *= sign 

        if res < -2**31 or res > 2**31 - 1:
            return 0
            
        return res
        
