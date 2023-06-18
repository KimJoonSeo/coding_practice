from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        for i in range(1, n):
            target = triangle[i]
            n2 = len(target)
            for j in range(n2):
                if j == 0:
                    target[j] += triangle[i-1][j]
                elif j == n2-1:
                    target[j] += triangle[i-1][j-1]
                else:
                    target[j] += min(triangle[i-1][j], triangle[i-1][j-1])



        return min(triangle[-1])


print(Solution().minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))