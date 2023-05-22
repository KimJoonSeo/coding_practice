from math import log2


class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        while n > 0:
            if log2(n) == int(log2(n)):
                return res + 1
            x = int(log2(n))
            # 여기가 포인트!!
            # n보다 제일 가까운 2개의 2의 거듭 제곱수 사이에서 차이가 적은 수를 n으로 바꾼다.
            n = min(abs(n-2**x), abs(n-2**(x+1)))
            res += 1
        return res

print(Solution().minOperations(3))