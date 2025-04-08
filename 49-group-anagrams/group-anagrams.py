class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d= {}
        res = []

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in d:
                i = d[sorted_s]
                res[i].append(s)
            else:
                d[sorted_s] = len(res)
                res.append([s])

        return res
            