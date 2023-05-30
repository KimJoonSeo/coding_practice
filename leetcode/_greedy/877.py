from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice = 0
        bob = 0

        while piles:
            if piles[0] > piles[-1]:
                alice += piles.pop(0)
            else:
                alice += piles.pop()

            if piles[0] > piles[-1]:
                bob += piles.pop()
            else:
                bob += piles.pop(0)
        return alice > bob
