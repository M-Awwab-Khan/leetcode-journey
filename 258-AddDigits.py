class Solution:
    def addDigits(self, num: int) -> int:
        # def break_and_add(num):
        #     if num == 0: return 0
        #     return break_and_add(num//10) + num%10
        # result = break_and_add(num)
        # while result // 10 != 0:
        #     result = break_and_add(result)
        # return result

        # The trick (digital root)
        return 0 if num == 0 else (9 if num % 9 == 0 else num %9)