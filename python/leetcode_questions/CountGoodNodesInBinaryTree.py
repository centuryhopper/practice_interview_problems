from data_structures import TreeNode

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        Use DFS (Depth First Search) to traverse the tree, and constantly keep track of the current path maximum.
        '''
        def rec(root,curMax) -> int:
            if not root: return 0
            curMax = max(curMax, root.val)
            l = rec(root.left,curMax)
            r = rec(root.right,curMax)
            if root.val >= curMax:
                return l + 1 + r
            return l + r
        return rec(root,root.val)






