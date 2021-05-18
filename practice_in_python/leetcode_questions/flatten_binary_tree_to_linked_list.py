from data_structures import TreeNode

class Solution:

    def f(self, root, conn) -> TreeNode:
        if not root:
            return conn
        tmp = root.right
        if tmp:
            conn = self.f(root.right, conn)
        root.right = self.f(root.left, conn)
        # remove left side connection
        root.left = None
        return root

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        root = self.f(root, None)