from collections import Counter
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        res = 0
        for k in list(counter.keys()):
            quotient, remainder = divmod(counter[k], k+1)
            res += (quotient *(k+1))
            if remainder:
                res += (k+1)

        return res