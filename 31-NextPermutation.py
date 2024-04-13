class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while nums[i] >= nums[i+1] and i >= 0:
            i -= 1

        if i < 0:
            nums.reverse()

        else:
            j = n - 1
            while nums[j] <= nums[i] and j > i:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            nums[i+1:] = nums[i+1:][::-1]

