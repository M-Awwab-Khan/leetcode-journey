class Solution:
    def myPow(self, x: float, n: int) -> float:
        e = abs(n)
        if e == 0:
            return 1
        half, remainder = divmod(e, 2)
        result = self.myPow(x, half)
        result *= result
        result = x * result if remainder else result
        result = 1/result if n < 0 else result
        return result
