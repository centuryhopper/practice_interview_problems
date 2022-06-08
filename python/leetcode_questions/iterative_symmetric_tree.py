#region
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#endregion
from collections import deque

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        # empty tree is a valid symmetric tree
        # because it's vacuously true!
        if root is None: return True

        # create two queues,
        # one to handle the left subtree, and the
        # other to handle the right
        l = deque()
        l.append(root.left)
        r = deque()
        r.append(root.right)


        # while both still have nodes to process
        while l and r:
            n1 = l.popleft()
            n2 = r.popleft()

            # if one of them is null, return false
            if (n1 != None and n2 == None) or (n1 == None and n2 != None):
                return False

            # if n1 is not null then n2 is also not null
            if n1 != None:
                if n1.val != n2.val:
                    return False
                l.append(n1.left)
                l.append(n1.right)
                r.append(n2.right)
                r.append(n2.left)
        return True