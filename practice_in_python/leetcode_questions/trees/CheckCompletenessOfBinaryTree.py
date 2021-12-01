# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    '''
    [1,2,3,5,null,7,8]
    [1,2,3,5,null,7]
    [1,2,3,4,5,6,7,8,9,10,11,12,13,null,null,15]
    '''
    # level-order traversal starting from the right
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        # if not root.left and not root.right: return True
        q = collections.deque([root])
        # if there's another level below
        # then the current level MUST be completely filled
        # expected number of nodes at the ith level while i < height of tree is 2**level
        level = 0
        while q:
            # num nodes on the current level
            n = len(q)
            seenLeft = seenRight = False
            for _ in range(n):
                cur = q.popleft()
                if cur.right:
                    q.append(cur.right)
                    seenRight = True
                else:
                    if seenLeft or seenRight:
                        return False
                if cur.left:
                    q.append(cur.left)
                    seenLeft = True
                else:
                    if seenRight:
                        return False
            # if there are more levels left,
            # then we check with our formula
            if q:
                if n != 2**level:
                    # print(n)
                    return False
            level+=1

        return True

