class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            answer = -int(str(abs(x))[::-1])
            if answer < -2**31:
                return 0
        else:
            answer = int(str(abs(x))[::-1])
            if answer > (2**31) - 1:
                return 0
        return answer
