from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        for i in range(m, n+m):
            nums1[i] = nums2[i-m]
        p1 = 0
        p2 = m
        while p1 < p2 and p2 < m+n:
            if nums1[p1] > nums1[p2]:
                temp = nums1[p1]
                nums1[p1] = nums1[p2]
                nums1[p2] = temp
            if p1 + 1 == p2:
                p1 += 1
                p2 += 1
            else:
                p1 += 1
        print(nums1)

Solution().merge(nums1 = [0], m = 0, nums2 = [1], n = 1)