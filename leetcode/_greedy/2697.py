class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = [None for _ in range(n)]
        if n % 2 == 1:
            ans[n//2] = s[n//2]
        for i in range(n//2):
            minimum = min(s[i], s[n-i-1])
            ans[i] = minimum
            ans[n-i-1] = minimum
        return ''.join(ans)
