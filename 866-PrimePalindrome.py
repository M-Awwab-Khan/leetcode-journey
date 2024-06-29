class Solution:
    def is_prime(self, n:int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True

        if (n % 2 == 0) or (n % 3 == 0):
            return False
        for i in range(5, int(sqrt(n)) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False

        return True

    def primePalindrome(self, n: int) -> int:
        if(n <= 2): return 2
        if(n >= 9989900): return 100030001
        if(n <= 11 and self.is_prime(n)): return n
        while True:
            if self.is_prime(n) and str(n) == str(n)[::-1]:
                return n
            n = n + 1