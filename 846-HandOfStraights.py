class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        freq = collections.Counter(hand)
        for card in hand:
            if freq[card] == 0:
                continue
            for i in range(groupSize):
                if freq[card + i] > 0:
                    freq[card + i] -= 1
                else:
                    return False
        return True