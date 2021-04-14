from data_structures import TreeNode as t
class Solution:
    def trimBST(self, root: t.TreeNode, lo: int, hi: int) -> TreeNode:

        if not root: return root

        # value too low, then answer is in right subtree
        if root.val < lo:
            return self.trimBST(root.right, lo, hi)

        # value too high, then answer is in left subtree
        elif root.val > hi:
            return self.trimBST(root.left, lo, hi)

        root.left = self.trimBST(root.left, lo, hi)
        root.right = self.trimBST(root.right, lo, hi)

        return root






































# def helper(root: TreeNode, rootParent: TreeNode, lo, hi) -> None:
#             if not root: return
#             # out of range
#             if root.val < lo or root.val > hi:
#                 if root != rootParent:
#                     if rootParent.val > root.val:
#                         rootParent.left = None
#                     else:
#                         rootParent.right = None
#                     helper(root.left, rootParent, lo, hi)
#                     helper(root.right, rootParent, lo, hi)
#                 else:
#                     print('here')
#                     if root.left and root.right:
#                         root = root.left if root.left.val > root.right.val else root.right
#                     elif root.left:
#                         root = root.left
#                     elif root.right:
#                         root = root.right
#                     helper(root.left, root, lo, hi)
#                     helper(root.right, root, lo, hi)
#             else:
#                 if root != rootParent:
#                     if root.val < rootParent.val:
#                         rootParent.left = root
#                     else:
#                         rootParent.right = root
#                 helper(root.left, root, lo, hi)
#                 helper(root.right, root, lo, hi)

#         helper(root, root, lo, hi)

#         return root

