class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx = 0
        l = 0
        n = len(height)
        r = n - 1
        while l < r:
            area = min(height[r], height[l]) * (r-l)
            mx = max(mx, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        

        return mx
