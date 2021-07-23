
from data_structures import TreeNode

#region my solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        '''
        If leaf node: return current value up
        Otherwise DFS left and right subtree

        If left subtree has no ones: root.left = None
        If right subtree has no ones: root.right= None

        If left and right subtrees are now both null, then return root.val
        Else: return 1
        '''
        def rec(root)->int:
            if not root:return 0
            l = rec(root.left)
            r = rec(root.right)
            if l == 0: root.left = None
            if r == 0: root.right = None
            # if it's now a leaf node, then tell parent whatever value you are
            if not root.left and not root.right:
                return root.val
            # otherwise we know there is a 1 somewhere in the subtree, so tell parent not
            # to remove this subtree
            return 1
        rec(root)
        if not root.left and not root.right and root.val == 0: return None
        return root
#endregion


#region faster online solution
# def pruneTree(self, root: TreeNode) -> TreeNode:
#         if not root:
#           return None
#         root.left = self.pruneTree(root.left)
#         root.right = self.pruneTree(root.right)
#         if root.val == 0 and not root.left and not root.right:
#           return None
#         return root
#endregion