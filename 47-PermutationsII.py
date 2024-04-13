from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        s = set()
        for i in permutations(nums, len(nums)) :
            if i not in s :
                s.add(i)
        return list(s)
