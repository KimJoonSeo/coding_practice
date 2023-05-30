import itertools
from typing import List



class Solution:
    def getValue(self, nums1, nums2, arr):
        a = 0
        for i in arr:
            a += nums1[i]
        b = nums2[arr[0]]
        for i in arr:
            b = min(b, nums2[i])
        return a*b

    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0
        n = len(nums1)
        indices = [i for i in range(n)]
        nCr = itertools.combinations(indices, k)
        for arr in nCr:
            res = max(res, self.getValue(nums1, nums2, arr))
        return res

print(Solution().maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3))