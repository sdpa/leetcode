class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def isValid(seg):
            if len(seg) > 1 and seg[0] == '0':
                return False
            return int(seg) <= 255

        def restore(level, s, ans):
            if level == 5:
                if s == "":
                    return [".".join(ans)]
                return []

            local_segs = []

            for i in range(1, 4):
                if len(s) >= i:
                    seg = s[:i]
                    remaining = s[i:]

                    if isValid(seg):
                        ans.append(seg)
                        segs = restore(level + 1, remaining, ans)
                        local_segs += segs
                        ans.pop()

            return local_segs

        return restore(1, s, [])

        


