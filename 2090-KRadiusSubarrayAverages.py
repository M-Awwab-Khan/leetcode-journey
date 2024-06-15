class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ws = 2*k + 1
        n = len(nums)
        s = 0
        result = [-1] * n
        
        for i in range(n):
            s += nums[i]
            if i >= ws - 1:
                result[i - (ws//2)] = s // ws
                s -= nums[i - ws + 1]

        return result

