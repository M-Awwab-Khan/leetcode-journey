class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        hm = {}
        for i in range(isqrt(c)+1):
            hm[i*i] = 1
            if c - i*i in hm:
                return True
        return False