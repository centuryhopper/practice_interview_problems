from collections import deque
from data_structures import TreeNode

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        # outer list
        retVal = []
        # inner list
        lst = []
        d = deque([root, None])
        while d:
            node = d.popleft()
            if node:
                # append to inner list and include its children in the deque waiting to be
                # processed, if a child exists
                lst.append(node.val)
                if node.left: d.append(node.left)
                if node.right: d.append(node.right)
            else:
                # we've come across a null value, so add our list to
                # the return value
                retVal.append(lst)
                # make a new one for the next level of nodes
                lst = []
                # cover for edge case of having processed every node already.
                # At that point the deque should be empty as we are currently
                # in the state of popping off the last null value. In all other cases,
                # this appends a null value to the end of the deque to signal that the
                # next level of nodes have been processed when we pop and get to this null value
                if d: d.append(None)
        return retVal




'''
Online more optimized solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        di=defaultdict(list)
        def solve(root,level,di):
            if not root:return
            di[level].append(root.val)
            if root.left:solve(root.left,level+1,di)
            if root.right:solve(root.right,level+1,di)
        solve(root,0,di)
        lis=list(di.keys())
        lis.sort()
        ans=[]
        for i in lis:
            ans.append(di[i])
        return ans
'''