from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        cnt = 0
        res = 0
        s, e = 0, len(tokens)-1

        while s <= e:
            if power >= tokens[s]:
                cnt += 1
                res = max(cnt, res)
                power -= tokens[s]
                s += 1
            elif power < tokens[s] and cnt >= 1:
                cnt -= 1
                power += tokens[e]
                e -= 1
            else:
                return res
        return res