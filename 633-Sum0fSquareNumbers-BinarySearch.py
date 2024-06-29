class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(math.sqrt(c))
        while a <= b:
            sq = a**2 + b**2
            if sq == c:
                return True
            elif sq > c:
                b -= 1
            else:
                a += 1
        return False