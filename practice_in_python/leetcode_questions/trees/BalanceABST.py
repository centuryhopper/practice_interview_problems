# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    maintain avl-tree property
    [1,2,3,4]
    '''
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def bstToArray(root) -> list[int]:
            if not root:
                return []
            ans = []
            ans.extend(bstToArray(root.left))
            ans.append(root.val)
            ans.extend(bstToArray(root.right))
            return ans
        def bstInsert(root,val) -> TreeNode:
            if not root:
                return TreeNode(val)
            if val < root.val:
                root.left = bstInsert(root.left,val)
            elif val > root.val:
                root.right = bstInsert(root.right,val)
            return root

        lst = bstToArray(root)
        newRoot = None
        def arrayToBalancedBST(lst)->None:
            nonlocal newRoot
            if not lst:
                return
            lo,hi = 0,len(lst)-1
            mid = lo+((hi-lo)//2)
            newRoot = bstInsert(newRoot,lst[mid])
            arrayToBalancedBST(lst[:mid])
            arrayToBalancedBST(lst[mid+1:])

        arrayToBalancedBST(lst)

        return newRoot



