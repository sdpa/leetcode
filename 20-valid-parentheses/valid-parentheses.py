class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = []

        for bracket in s:
            if bracket in pairs.values():
                stack.append(bracket)
            elif len(stack) > 0 and pairs[bracket] == stack[-1]:
                    stack.pop(-1)
            else: return False
        
        return len(stack) == 0



        