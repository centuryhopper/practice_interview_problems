# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def level_by_level(root: TreeNode, d: deque[TreeNode]) -> list[int]:
            if not root:
                return
            d.append(root)
            d.append(None)
            lst = []
            while d:
                item = d[0]
                d.popleft()
                if not item:
                    print()
                    d.append(None)
                    # no more node values to print, so we return out
                    if len(d) == 1:
                        break
                else:
                    print(item.val, end=' ')
                    # if the next front of queue is None
                    # then we know we just printed the last element
                    if not d[0]:
                        lst.append(item.val)
                    if item.left:
                        d.append(item.left)
                    if item.right:
                        d.append(item.right)

            return lst

        d = deque()
        return level_by_level(root, d)
