class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while stack and digit < stack[-1] and k:
                stack.pop()
                k -= 1
            stack.append(digit)

        stack = stack[:-k] if k > 0 else stack

        res = ''.join(stack).lstrip('0')
        return res if res != '' else '0'
