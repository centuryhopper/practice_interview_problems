# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import functools

class Solution:
    '''
                           1
                        /     \
                       1       10
                      /       /
                     5       30
    
    '''
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @functools.lru_cache(None)
        def rec(root,didStealFromParent) -> int:
            if not root: return 0
            if not didStealFromParent:
                steal = root.val + rec(root.left,True) + rec(root.right,True)
                notSteal = rec(root.left,False) + rec(root.right,False)
                return max(steal,notSteal)
            return rec(root.left,False) + rec(root.right,False)
        
        return max(rec(root,True),rec(root,False))