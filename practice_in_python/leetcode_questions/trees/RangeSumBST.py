# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from data_structures import TreeNode
from typing import Optional

class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        def rec(root,low,high)->int:
            if not root: return 0
            total = 0
            # too small => go right
            if root.val < low:
                total += rec(root.right,low,high)
            # too big => go left
            elif root.val > high:
                total += rec(root.left,low,high)
            # in range => search both directions
            else:
                total += root.val + rec(root.left,low,high) + rec(root.right,low,high)
            return total

        return rec(root,low,high)


