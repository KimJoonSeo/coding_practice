class Solution:
    def countHomogenous(self, s: str) -> int:
        prev = None
        cnt = 0
        records = []
        for c in s:
            if prev != c:
                prev = c
                if cnt:
                    records.append(cnt)
                cnt = 1
            else:
                cnt += 1
        if cnt:
            records.append(cnt)

        res = 0
        for r in records:
            res += ((r*(r+1) // 2) % (10**9 + 7))
        return res
