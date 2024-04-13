from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combos = []
        present = []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        for char in digits:
            present.append(mapping[char])
        
        def join(itr):
            return ''.join(itr)
        return list(map(join, product(*present)))
