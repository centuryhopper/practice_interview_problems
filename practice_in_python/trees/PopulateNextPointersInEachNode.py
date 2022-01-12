"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        q = collections.deque([root,None])
        nxt = None
        while True:
            cur = q.popleft()
            if not cur:
                if not q:
                    break
                q.append(None)
                continue
            nxt = q[0]
            cur.next = nxt
            if cur.left: q.append(cur.left)
            if cur.right: q.append(cur.right)
        return root