class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        neg = True if x < 0 else False
        x = abs(x)

        multiplier = 1
        while(x > 0):
            remainder = x % 10
            x = x // 10
            if res > (2**31 - 1) // 10:
                return 0  
            res = (res * multiplier) + remainder 
            multiplier = max(multiplier, 10)

        if(neg):
            return -1 * res
        return res