class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def feasible(days):
            flower, bouquet = 0, 0
            for bloom in bloomDay:
                if bloom > days:
                    flower = 0
                else:
                    flower += 1
                    if flower // k == 1:
                        flower = 0
                        bouquet += 1
                    
            return bouquet < m

        n = len(bloomDay)
        if m*k > n:
            return -1
        l, r = 1, max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            if feasible(mid):
                l = mid + 1
            else:
                r = mid
        return l