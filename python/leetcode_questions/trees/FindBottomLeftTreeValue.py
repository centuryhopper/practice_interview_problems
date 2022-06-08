# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        '''reversed level-order traversal'''
        # if not root: return
        q = collections.deque([root])
        ans = root.val
        while q:
            cur = q[0]
            n = len(q)
            for _ in range(n):
                cur = q.popleft()
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
            if not q:
                ans = cur

        return ans.val
