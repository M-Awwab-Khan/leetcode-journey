class Solution:
    def isThree(self, n: int) -> bool:
        if n <= 3:
            return False

        divisors = 2
        for i in range(2, n):
            if n % i == 0:
                divisors += 1
            if divisors > 3:
                return False

        return divisors == 3