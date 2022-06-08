# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from data_structures import TreeNode
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def rec(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return rec(p.left,q.left) and rec(p.right,q.right)
        return rec(p,q)
        
            