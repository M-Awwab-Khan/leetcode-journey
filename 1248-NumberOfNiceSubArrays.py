class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def atmostK(k):
            result = 0
            odds = 0
            left = 0
            for right in range(n):
                if nums[right] % 2 != 0:
                    odds += 1
            
                while odds > k:
                    if nums[left] % 2 != 0:
                        odds -= 1
                    left += 1

                result += right - left + 1
            return result

        return atmostK(k) - atmostK(k - 1)