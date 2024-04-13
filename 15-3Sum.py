class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        a = sorted([nums[i], nums[j], nums[k]])
                        if a not in triplets:
                            triplets.append(a)
        return triplets

