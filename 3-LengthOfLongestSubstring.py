class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        left = 0
        seen = set()

        for right in range(n):
            # If the current character is already in the set,
            # move the left pointer until the character is removed from the set.
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            # Add the current character to the set.
            seen.add(s[right])
            
            # Update the maximum length if needed.
            max_length = max(max_length, right - left + 1)

        return max_length
