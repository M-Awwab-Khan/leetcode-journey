import re
class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.search(r'^\s*([-+]?\d+)', s)
        if match:
            INT_MAX = 2**31
            num_str = match.group(1)
            result = int(num_str)
            if result < -INT_MAX:
                return -INT_MAX
            elif result > (INT_MAX) - 1:
                return (INT_MAX) - 1
            return result
        return 0