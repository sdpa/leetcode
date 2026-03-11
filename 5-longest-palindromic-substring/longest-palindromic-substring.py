class Solution:
    def longestPalindrome(self, s: str) -> str:

        def getPalindrome(left, right, s):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        res = ""
        for i in range(len(s)):
            # Expand from center and check if its palindrome
            s_a = getPalindrome(i, i, s)
            s_b = getPalindrome(i, i+1, s)
            if len(s_a) > len(res):
                res = s_a
            if len(s_b) > len(res):
                res = s_b
        return res
            


        