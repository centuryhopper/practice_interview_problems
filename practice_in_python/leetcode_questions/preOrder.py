# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        lst = []
        if not root: return lst
        l = [root]
        while l:
            node = l.pop()
            lst.append(node.val)
            if node.right:
                l.append(node.right)
            if node.left:
                l.append(node.left)
        return lst
        
        