class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hs = set(nums)
        longest_streak = 1
        for num in hs:
            if num - 1 not in hs:
                current = num
                current_streak = 1
                while current + 1 in hs:
                    current_streak += 1
                    longest_streak = max(longest_streak, current_streak)
                    current += 1

        return longest_streak