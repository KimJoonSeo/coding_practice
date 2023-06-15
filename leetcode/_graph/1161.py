import heapq
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        lv_cnt = {}
        q = deque()
        q.append((1, root))

        while q:
            lv, node = q.popleft()
            lv_cnt[lv] = lv_cnt.get(lv, 0) + node.val

            if node.left:
                q.append((lv+1, node.left))
            if node.right:
                q.append((lv+1, node.right))

        res = 1
        max_val = root.val
        for k in list(lv_cnt.keys()):
            if max_val < lv_cnt[k]:
                res = k
                max_val = lv_cnt[k]
        return res