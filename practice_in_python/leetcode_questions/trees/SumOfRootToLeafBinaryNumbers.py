# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0
        def rec(root,path):
            nonlocal total
            if not root:
                return
            rec(root.left,path+[str(root.val)])
            rec(root.right,path+[str(root.val)])
            if not root.left and not root.right:
                total += int(''.join(path+[str(root.val)]),2)
        rec(root,[])
        return total
