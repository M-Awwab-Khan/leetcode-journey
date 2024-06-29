class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = float('inf')
        mx = -float('inf')
        for num in nums:
            mn = min(mn, num)
            mx = max(mx, num)

        return math.gcd(mn, mx)