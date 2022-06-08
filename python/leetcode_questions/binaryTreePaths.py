from data_structures import TreeNode

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        mainLst = []
        def rec(root, lst):
            nonlocal mainLst
            if not root: return
            rec(root.left,lst + [f'{root.val}'])
            if not root.left and not root.right:
                mainLst.append('->'.join(lst + [f'{root.val}']))
            rec(root.right,lst + [f'{root.val}'])
        rec(root, [])
        return mainLst

        