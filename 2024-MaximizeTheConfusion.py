class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        Tmax = self.solve(answerKey, k, 'T')
        Fmax = self.solve(answerKey, k, 'F')

        return max(Tmax, Fmax)

    def solve(self, answerKey: str, k: int, opt: str) -> int:
        maxi = -1
        n = len(answerKey)
        k2 = 0
        i = 0
        for j in range(n):
            if answerKey[j] != opt:
                k2 += 1
            while k2 > k:
                if answerKey[i] != opt:
                    k2 -= 1
                i += 1
            maxi = max(j - i + 1, maxi)
        return maxi