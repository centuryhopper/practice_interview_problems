# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
BST solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def rec(root,p,q)->TreeNode:
            if not root: return None
            # if root val is smaller than both, go right
            if root.val < p.val and root.val < q.val:
                return rec(root.right,p,q)
            # if root val is greater than both, go left
            if root.val > p.val and root.val > q.val:
                return rec(root.left,p,q)
            # else current root must be the lowest common ancestor
            return root
        return rec(root,p,q)
'''
# BT solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def rec(root,p,q)->TreeNode:
            if not root: return None
            if root == p or root == q:
                return root
            left = rec(root.left,p,q)
            right = rec(root.right,p,q)
            # both have something to offer
            if left and right:
                return root            
            # left subtree has something to offer
            if left:
                return left
            # right subtree has something to offer
            if right:
                return right
            # neither have anything to offer
            return None
        
        
        return rec(root,p,q)