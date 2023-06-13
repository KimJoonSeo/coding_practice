from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 1
        s = 0
        e = arr[0]
        n = len(arr)

        for i in range(1, n):
            if i == arr[i] and e < i:
                res += 1
                s = i
                e = i
            elif i != arr[i]:
                if e < i and e < arr[i]:
                    res += 1
                    s = min(i, arr[i])
                    e = max(i, arr[i])
                else:
                    s = min(s, i, arr[i])
                    e = max(e, i, arr[i])
        return res
