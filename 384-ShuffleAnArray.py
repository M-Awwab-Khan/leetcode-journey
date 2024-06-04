from random import sample
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.len = len(nums)

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        return sample(self.nums, self.len)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()