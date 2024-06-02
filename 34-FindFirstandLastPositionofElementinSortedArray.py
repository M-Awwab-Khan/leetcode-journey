class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            if (nums[i] == target):
                j = i
                while j < n-1 and nums[j+1] == nums[i]:
                    j += 1
                else:
                    return [i , j]
        
        return [-1, -1]