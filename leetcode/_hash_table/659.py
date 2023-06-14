from collections import defaultdict, Counter
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        seq = defaultdict(int)
        left = Counter(nums)

        for n in nums:
            if left[n] == 0:
                continue

            if seq[n-1] > 0:
                seq[n-1] -= 1
                seq[n] += 1
                left[n] -= 1
            else:
                # 새로 만들기
                if left[n+1] < 1 or left[n+2] < 1:
                    return False
                left[n] -= 1
                left[n+1] -= 1
                left[n+2] -= 1
                seq[n+2] += 1
        return True