# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from data_structures import TreeNode
from collections import deque


# region final solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def rec(root, p, q) -> TreeNode:
            if not root:
                return None
            # equal case
            if root.val == p.val or root.val == q.val:
                return root
            # not equal case
            # check left subtree
            # and right subtree
            l = rec(root.left, p, q)
            r = rec(root.right, p, q)
            # found lowest common ancestor
            # because both left and right subtrees returned a non-null value
            if l and r:
                return root
            # l has something to offer,
            # so return it to its parent
            if l:
                return l
            # l had nothing to offer,
            # but r has something to offer,
            # so return it to its parent
            if r:
                return r

            # both left and right subtree
            # have nothing to offer,
            # so return null back up to parent
            return None
        return rec(root, p, q)
# endregion


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # def rec(a, p, q) -> bool:
        #     if not a: return False
        #     if a == q: return True
        #     # if there's a path from p to q, return p (vice versa is true too)
        #     return rec(a.left,p,q) or rec(a.right,p,q)
        # # direct relationship check
        # if rec(p,p,q): return p
        # if rec(q,q,p): return q

        # level order traversal
        d = {}
        l = deque([(root, None), (None, None)])
        cnt = 0
        while l:
            node, parent = l.popleft()
            if not node:
                cnt += 1
                l.append((None, None))
                if len(l) == 1:
                    break
            else:
                # used to be d[node.val]
                d[node.val] = (cnt, parent)
                if node.left:
                    l.append((node.left, node))
                if node.right:
                    l.append((node.right, node))
        # print(d[p][1], d[q][1])
        print(d)
        common = None

        def getCommon(p, q) -> None:
            nonlocal d, common
            # recursed to a common ancestor
            if p == q:
                common = p
                return
            if not d[p][1] or not d[q][1]:
                return
            # move only p up the tree
            getCommon(d[p][1], q)
            # move only q up the tree
            getCommon(d, d[q][1])
            # move both up the tree
            getCommon(d[d][1], d[q][1])
        getCommon(p, q)

        return common

    # region TLE solution
    '''
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # def rec(a, p, q) -> bool:
        #     if not a: return False
        #     if a == q: return True
        #     # if there's a path from p to q, return p (vice versa is true too)
        #     return rec(a.left,p,q) or rec(a.right,p,q)
        # # direct relationship check
        # if rec(p,p,q): return p
        # if rec(q,q,p): return q
        
        # level order traversal
        d = {}
        l = deque([(root, None),(None,None)])
        cnt = 0
        while l:
            node, parent = l.popleft()
            if not node:
                cnt+=1
                l.append((None,None))
                if len(l) == 1: break
            else:
                # used to be d[node.val]
                d[node] = (cnt,parent)
                if node.left: l.append((node.left, node))
                if node.right: l.append((node.right, node))
        common = []
        def getCommon(p,q)->None:
            nonlocal d,common
            # recursed to a common ancestor
            if p == q:
                common.append((d[p][0], p))
                return
            if not p or not q:
                return
            # move only p up the tree
            getCommon(d[p][1], q)
            # move only q up the tree
            getCommon(p, d[q][1])
            # move both up the tree
            getCommon(d[p][1],d[q][1])
        getCommon(p,q)
        # for x, _ in common:
        #     print(x)
        return max(common, key=lambda t:t[0])[1]
    '''
    # endregion
