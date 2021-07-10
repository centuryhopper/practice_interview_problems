from data_structures import TreeNode

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def rec(root, curSum, targetSum) -> bool:
            # empty tree/going out of bounds case
            if not root:
                return False
            # potential success case
            if not root.left and not root.right:
                # include the last node in the current sum as well
                if curSum + root.val == targetSum:
                    return True
                return False
            return rec(root.left, curSum + root.val, targetSum) or rec(root.right, curSum + root.val, targetSum)

        return rec(root, 0, targetSum)
