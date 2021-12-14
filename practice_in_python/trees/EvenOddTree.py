
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        '''level-order traversal'''
        if not root: return True
        level = 0
        prev = float('-inf')
        q = collections.deque([root,None])
        while True:
            cur = q.popleft()
            if not cur:
                if not q:
                    break
                q.append(None)
                level+=1
                if level&1:
                    prev = float('inf')
                else:
                    prev = float('-inf')
                continue
            if level&1:
                if cur.val&1 or cur.val >= prev:
                    return False
            else:
                if not cur.val&1 or cur.val <= prev:
                    return False
            prev = cur.val
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return True



