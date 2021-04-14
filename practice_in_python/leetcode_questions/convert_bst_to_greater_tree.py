# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# the key to this problem is to perform a reverse inorder traversal of the tree
class Solution:
    def __init__(self):
        self.acc = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        # implementation
        def reverse_inorder(root: TreeNode) -> None:
            if not root:
                return
            reverse_inorder(root.right)
            root.val += self.acc
            self.acc = root.val
            reverse_inorder(root.left)

        reverse_inorder(root)

        return root
