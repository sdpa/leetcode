class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEat(piles, k):
            total_hours = 0
            for pile in piles:
                if pile < k:
                    total_hours += 1
                else:
                    total_hours += math.ceil(pile / k)
            return total_hours <= h

        left = 1
        right = max(piles)
        res = right
        while left <= right:
            k = (right + left) // 2  

            if canEat(piles, k):
                right = k - 1
                res = min(res, k)
            else:
                left = k + 1
        
        return res
        