# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
               1
              /
             2
            /
           3
          /
         4
        /
       5
'''


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # came from left => 1
        ans = 0
        def rec(root, left):
            nonlocal ans
            if not root:
                return None
            # if we've came from the left and the current node is childless
            if left == 1 and not root.left and not root.right:
                ans += root.val
            # tell the children calls that a 1 means it's a relative child and 0 means it's not
            rec(root.left, 1)
            rec(root.right, 0)
            # matching case (This check doesn't work for some reason)
            # fails on this tree:
            '''
            [5,0,-4,-1,-6,-9,null,7,null,1,3,null,0,null,9,null,null,6,0,null,-7,null,null,null,null,null,null,-4,null,1,null,null,-4]
            '''
            # if left == 1 and not l and not r:
            #     ans+=root.val
            return root

        rec(root, 0)

        return ans
