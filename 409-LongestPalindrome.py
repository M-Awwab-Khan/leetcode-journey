from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        result = 0
        has_odd = False
        for char, count in freq.items():
            if count % 2 == 0:
                result += count
            if count % 2 == 1:
                result += count - 1
                has_odd = True
        return result if not has_odd else result + 1