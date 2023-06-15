import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)

        main_heap = []
        for key in list(counter.keys()):
            heapq.heappush(main_heap, (-counter[key], key))
        res = ''
        while main_heap:
            if len(main_heap) == 1:
                return ''
            first = heapq.heappop(main_heap)
            second = heapq.heappop(main_heap)
            res += first[1]
            res += second[1]
            if first[0]+1:
                heapq.heappush(main_heap, (first[0]+1, first[1]))
            if second[0]+1:
                heapq.heappush(main_heap, (second[0]+1, second[1]))

        return res

print(Solution().reorganizeString(s = "aaab"))



