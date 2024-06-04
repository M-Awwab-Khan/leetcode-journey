class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        lens, lent = len(s), len(t)
        s0, t0 = 0, 0

        while s0 < lens and t0 < lent:
            if s[s0] == t[t0]:
                t0 += 1
            s0 += 1
        
        return lent - t0
        