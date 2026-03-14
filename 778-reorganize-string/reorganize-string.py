import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        # Use a heap to solve. 
        count = Counter(s)
        pq = []
        for c in count:
            heapq.heappush(pq, (-count[c], c))
        print(pq)
        prev = (0, '')
        res = ""
        while len(pq) > 0:
            (count, c) = heapq.heappop(pq)
            res += c
            if prev[0] < 0:
                heapq.heappush(pq, prev)
            count += 1
            prev = (count, c)
        
        res = ''.join(res)
        if len(res) != len(s): return ""
        return res
            



            
        



        