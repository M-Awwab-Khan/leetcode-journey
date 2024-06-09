class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if sum(math.ceil(pile/mid) for pile in piles) <= h:
                r = mid
            else:
                l = mid + 1
        return l