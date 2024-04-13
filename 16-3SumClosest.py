from math import inf
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = inf
        n = len(nums)
        for a in range(n - 2):
            l = a + 1
            r = n - 1
            while l < r:
                curr_sum = nums[a] + nums[l] + nums[r]
                if curr_sum == target:
                    return target
                else:
                    if abs(target-curr_sum) < diff:
                        diff = abs(target-curr_sum)
                        close_sum = curr_sum
                    if curr_sum > target:
                        r -= 1
                    elif curr_sum < target:
                        l += 1
            
        return close_sum

