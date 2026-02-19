class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        first = strs[0]
        last = strs[-1]

        l = min(len(first), len(last))

        i = 0
        res = ""
        while(i < l):
            if first[i] == last[i]:
                res += first[i]
                i += 1
            else:
                break
        return res
        