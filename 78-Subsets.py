from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = [[], nums]
        for i in range(1, len(nums)):
            powerset.extend(map(list, combinations(nums, i)))
        return powerset 
