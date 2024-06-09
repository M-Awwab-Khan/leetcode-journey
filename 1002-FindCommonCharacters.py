class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        answer = collections.Counter(words[0])
        for word in words[1:]:
            answer &= collections.Counter(word)
        return answer.elements()
        
        # return reduce(lambda a, b: a & b, map(collections.Counter, words)).elements()