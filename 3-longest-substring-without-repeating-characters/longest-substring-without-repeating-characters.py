class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        # Use 2 pointer solution.
        if len(s) <= 1:
            return len(s)
        left = 0 
        right = left

        max_len = 0
        count = {}
        while right < len(s):
            c = s[right]
            if c in count:
                left = max(left, count[c] + 1)
            count[c] = right
            right += 1
            max_len = max(max_len, right - left)
        return max_len
            


            
                



        