from data_structures import TreeNode

class Solution:

    # I would use level-order tree traversal for an iterative approach

    # assume a null tree never gets passed in and that d >= 1
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:

        if not root or d < 1:
            print('please make sure that your root is not null and your depth value (d) is at least 1')
            return None

        def helper(root: TreeNode, v: int, d: int) -> None:
            if not root:
                return
            if d == 2:
                l = TreeNode(v, root.left, None)
                root.left = l
                r = TreeNode(v, None, root.right)
                root.right = r
                return
            helper(root.left, v, d-1)
            helper(root.right, v, d-1)

        # edge case of d = 1
        if d == 1:
            newRoot = TreeNode(v, root, None)
            return newRoot

        # rewire nodes of all other depths
        helper(root, v, d)
        return root
