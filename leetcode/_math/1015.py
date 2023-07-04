class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        res = 1
        target = 1

        if k%10 in [0, 2, 4, 5, 6, 8]:
            return -1

        while True:
            if target % k == 0:
                return res
            res += 1
            target = target * 10 + 1
