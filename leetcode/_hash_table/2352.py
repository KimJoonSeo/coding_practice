from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        hash_map = {}
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(grid[j][i])
            t = tuple(temp)
            hash_map[t] = hash_map.get(t,0)+1
        res = 0
        for i in range(n):
            res += hash_map.get(tuple(grid[i]), 0)

        return res