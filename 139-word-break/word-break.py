class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # Check if any of the words start with that dctory element.
        memo = {}
        def helper(s, wordDict, memo):
            if s in memo:
                return memo[s]
            if s == "":
                memo[s] = True
                return True

            for word in wordDict:
                if s.startswith(word):
                    if(helper(s[len(word):], wordDict, memo)):
                        memo[s] = True
                        return True
                        
            memo[s] = False
            return False
        
        return helper(s, wordDict, memo)
