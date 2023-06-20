from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        if 2*k+1 > n:
            return [-1 for _ in range(n)]

        presum = sum(nums[:2*k+1])
        res = [int(presum/(2*k+1))]
        first_idx = 1
        last_idx = 2*k+1

        while last_idx < n:
            presum -= nums[first_idx-1]
            presum += nums[last_idx]
            res.append(int(presum/(2*k+1)))
            first_idx += 1
            last_idx += 1
        return [-1 for _ in range(k)] + res + [-1 for _ in range(k)]

print(Solution().getAverages(nums = [8], k = 100000))