class Solution:
    def decodeString(self, s: str) -> str:
        def helper(s):
            # Find the set of characters that are a number
            k_str = ''
            res = ''
            i = 0
            while i < len(s):
                if ord(s[i]) >= 48 and ord(s[i]) <= 57:
                    k_str += s[i]
                    i += 1
                elif s[i] == '[':  # Go until the end and get the result of substring.
                    k = int(k_str)
                    k_str = ''
                    start = i
                    stack = []
                    stack.append(s[i])
                    i += 1
                    while len(stack) > 0:
                        if s[i] == '[':
                            stack.append(s[i])
                        elif s[i] == ']':
                            stack.pop(-1)
                        i += 1
                    sub_str = s[start+1:i-1]
                    decoded = helper(sub_str)

                    for _ in range(k):
                        res += decoded
                elif s[i] >= 'a' and s[i] <= 'z':
                    res += s[i]
                    i += 1
            return res

        return helper(s)