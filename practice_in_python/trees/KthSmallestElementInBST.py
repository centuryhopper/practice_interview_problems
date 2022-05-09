from typing import Optional
from ..data_structures import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # do inorder traversal and have a counter from 0 and stop when counter is k
        cnt = 0
        ans = -1
        def inorder(root):
            nonlocal cnt, ans
            if not root: return
            if ans != - 1: return
            inorder(root.left)
            cnt+=1
            if cnt == k:
                ans = root.val
            inorder(root.right)
        inorder(root)
        return ans



