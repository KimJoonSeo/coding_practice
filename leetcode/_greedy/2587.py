from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        prefix = 0
        res = 0
        for i in range(n):
            if prefix + nums[i] <= 0:
                return res
            prefix += nums[i]
            res += 1
        return res