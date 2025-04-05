class Solution:
    def getPalid(self,i, j, s):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i-=1
            j+=1
        return s[i+1:j]

    def longestPalindrome(self, s: str) -> str:
        # expand from center. 
        longest = ""
        if len(s) <= 1:
            return s
        for i in range(len(s)):
            even = self.getPalid(i, i, s)
            odd = self.getPalid(i, i + 1, s)

            if len(even) > len(odd):
                cur_longest = even
            elif len(odd) > len(even):
                cur_longest = odd

            if len(cur_longest) > len(longest):
                longest =   cur_longest      
        return longest

