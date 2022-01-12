# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def rec(root,val)->int:
            if not root:
                return 0
            cur = abs(val-root.val)
            return max(cur,rec(root.left,val), rec(root.right,val))


        if not root:
            return 0

        maxAtCur = max(rec(root.left,root.val),rec(root.right,root.val))

        return max(maxAtCur,self.maxAncestorDiff(root.left),self.maxAncestorDiff(root.right))


