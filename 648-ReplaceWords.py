class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sent = sentence.split()
        for i in range(len(sent)):
            for root in sorted(dictionary, key=len):
                if sent[i].startswith(root):
                    sent[i] = root
        return ' '.join(sent)