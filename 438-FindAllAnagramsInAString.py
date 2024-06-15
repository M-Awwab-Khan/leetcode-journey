class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lp = len(p)
        ls = len(s)
        if lp > ls: return []
        p_map = collections.Counter(p)
        res = []
        s_map = collections.Counter(s[0:0+lp])
        for i in range(ls - lp + 1):
            if s_map == p_map:
                res.append(i)
            if i+lp < ls:
                s_map[s[i]] -= 1
                s_map[s[i+lp]] += 1
        return res