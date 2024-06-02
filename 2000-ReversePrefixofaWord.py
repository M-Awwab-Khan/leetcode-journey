class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l = 0
        for r in range(len(word)):
            if word[r] == ch:
                break
        else:
            return word
        
        word = list(word)
        word[l:r+1] = word[l:r+1][::-1]
        return ''.join(word)