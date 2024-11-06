import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        
        while l <= r:
            mid = (l + r) // 2
            cnt = 0
            for pile in piles:
                cnt += math.ceil(pile / mid)

            if cnt > h:
                l = mid + 1
            else:
                r = mid - 1

        return l