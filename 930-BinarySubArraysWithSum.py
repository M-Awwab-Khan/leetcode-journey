class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        def atmostgoal(goal):
            res = 0
            left = 0
            curr_sum = 0
            for right in range(n):
                curr_sum += nums[right]
                
                while curr_sum > goal and left < right:
                    curr_sum -= nums[left]
                    left += 1

                if not (curr_sum > goal):
                    res += right - left + 1

            return res

        return atmostgoal(goal) - atmostgoal(goal-1)
                