class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sm = 0
        i = 0
        min_length = float('inf')
        for j in range(len(nums)):
            sm += nums[j]
            while sm >= target:
                min_length = min(min_length, j - i + 1)
                sm -= nums[i]
                i += 1
        
        return min_length if min_length != float('inf') else 0
                
        
        