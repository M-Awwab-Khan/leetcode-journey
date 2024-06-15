class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return [i**2 for i in sorted(nums, key=lambda x: abs(x))]