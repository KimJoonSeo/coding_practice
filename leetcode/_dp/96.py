class Solution:
    def numTrees(self, n: int) -> int:
        dp = {i:0 for i in range(n+1)}
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[n]

print(Solution().numTrees(3))