from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        counter = Counter(hand)

        for card in hand:
            if not counter[card]:
                continue

            counter[card] -= 1
            for i in range(1, groupSize):
                if not counter[card+i]:
                    return False
                counter[card+i] -= 1
        return True