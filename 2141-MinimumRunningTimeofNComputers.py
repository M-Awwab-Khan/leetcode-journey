class Solution:
    def maxRunTime(self, n, batteries):
        def canRunFor(t):
            total = 0
            for battery in batteries:
                total += min(battery, t)
            return total >= n * t

        left, right = 0, sum(batteries) // n
        while left < right:
            mid = (left + right + 1) // 2
            if canRunFor(mid):
                left = mid
            else:
                right = mid - 1

        return left