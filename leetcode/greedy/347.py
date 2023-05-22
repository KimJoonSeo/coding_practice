import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        for n in nums:
            hash_table[n] = hash_table.get(n, 0) + 1

        max_heap = []
        for key in list(hash_table.keys()):
            heapq.heappush(max_heap, (-hash_table[key], key))

        ans = []
        for _ in range(k):
            cnt, key = heapq.heappop(max_heap)
            ans.append(key)
        return ans

print(Solution().topKFrequent([1,1,1,2,2,3], 2))