class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if not r:
            return r
        while l < r:
            mid = (l + r) // 2
            if nums[mid + 1] > nums[mid]:
                l = mid + 1
                mid += 1
            elif nums[mid - 1] > nums[mid]:
                r = mid - 1
                mid -= 1
            else:
                return mid
        return l