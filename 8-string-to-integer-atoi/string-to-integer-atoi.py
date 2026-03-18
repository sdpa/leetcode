class Solution:
    def myAtoi(self, s: str) -> int:

        INT_MIN = -2 ** 31
        INT_MAX = (2** 31) - 1

        # Leading white space - so they are mostly in the front.
        i = 0
        while(i < len(s) and s[i] == " "):
            i += 1
        
        # Determine sign
        sign = 1
        if(i < len(s) and s[i] == '-'):
            sign = -1
            i += 1
        elif(i < len(s) and s[i] == '+'):
            sign = 1
            i += 1


        res = 0
        while(i < len(s)):
            if not s[i].isdigit():
                break
            res = res * 10 + int(s[i])
            i += 1

            if sign * res <= INT_MIN:
                return INT_MIN
            if sign * res >= INT_MAX:
                return INT_MAX
        
        return sign * res
        



        
        