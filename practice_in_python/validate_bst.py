# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root: TreeNode, min: Optional[int], max: Optional[int]) -> bool:
            if not root: return True
            if (min is not None and root.val <= min) or (max is not None and root.val >= max):
                return False
            flag = True

            flag &= helper(root.left, min, root.val)
            flag &= helper(root.right, root.val, max)

            return flag
        if not root: return True
        return helper(root.left, None, root.val) and helper(root.right, root.val, None)

print('hello')
