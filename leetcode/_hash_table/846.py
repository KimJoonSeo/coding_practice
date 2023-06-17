import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        n = len(s)
        res = [0 for _ in range(n)]

        max_key = None
        max_val = 0

        for key in list(counter.keys()):
            if counter[key] > max_val:
                max_key = key
                max_val = counter[key]
        try:
            for i in range(max_val):
                res[i*2] = max_key
            counter.pop(max_key)

            for i in range(n):
                if res[i]:
                    continue
                key = list(counter.keys())[0]
                if key == res[i-1]:
                    key = list(counter.keys())[1]
                res[i] = key
                if counter[key] == 1:
                    counter.pop(key)
                else:
                    counter[key] -= 1
        except Exception as e:
            return ''

        return ''.join(res)

print(Solution().reorganizeString("mjpssblxurlkotcdsvzfcpttkgoonesmzulotptbbjmmftxqkchbbbaddoyfkqwykriartdhcsxzeopeycdwwzueabsojppyhxrznxkzppyshukvxiszmrlzdcncrowaiwjehovhyictrholicfhdpsmjgmdjumhxujnaobzmfacxhpnpfvbxzhnnuzlpexfpqkcuusyeqabklkmxhpwybsmypttzcdzcmmkaoruxkqleomllnhhlgqggtoymgntzzxaxtdefpxdhgjqybkvcqzjegrvdviagjofvnxxonaknssdwcilwjkcwltbvgwiawvaehhhoxmmiyxntkztjbhovnpuynrkdqnjchpurwuywchjclvqqhbvvtqenyzudypfeyzwdnfozvozgzisyjqhzdbrilwyylyibfjvwfcsvfmngedhcufeprzrwvbhsezftisudgtecqszipqilqncelrmrjlwtopaweidhjuzdviehti"))