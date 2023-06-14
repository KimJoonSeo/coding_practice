from collections import Counter
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort()
        left = Counter(nums)

        for n in nums:
            if left[n] == 0:
                continue
            for i in range(n, n+k):
                if left[i] == 0:
                    return False
                left[i] -= 1
        return True
