from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        res = []
        pre_remainder = 0
        for i in range(n):
            _, remainder = divmod(pre_remainder*10 + int(word[i]), m)
            if remainder:
                res.append(0)
            else:
                res.append(1)
            pre_remainder = remainder
        return res