import heapq
from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        hash_map = {}

        for r in roads:
            s, e = r
            hash_map[s] = hash_map.get(s,0) + 1
            hash_map[e] = hash_map.get(e,0) + 1

        max_heap = []

        for k in list(hash_map.keys()):
            heapq.heappush(max_heap, (-hash_map[k], k))
        res = 0
        for _ in list(hash_map.keys()):
            cnt, val = heapq.heappop(max_heap)
            res += (-cnt*n)
            n -= 1
        return res