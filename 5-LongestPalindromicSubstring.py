class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            if s[left] != s[right]:
                return ''
            while left > 0 and right < len(s) - 1:
                left -= 1
                right += 1

                if s[left] != s[right]:
                    break
            else:
                return s[left: right+1]
            return s[left+1:right]
                    
        longest_str = s[0]
        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i+1)

            longest_str = odd if len(odd) > len(longest_str) else longest_str
            longest_str = even if len(even) > len(longest_str) else longest_str
        return longest_str
