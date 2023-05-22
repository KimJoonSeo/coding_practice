from math import log2


class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        while n > 0:
            if log2(n) == int(log2(n)):
                return res + 1
            x = int(log2(n))
            n = min(abs(n-2**x), abs(n-2**(x+1)))
            res += 1
        return res

print(Solution().minOperations(3))