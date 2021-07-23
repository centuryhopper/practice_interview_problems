# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # brute force would be to use hashmap to keep track of number frequency
    # we will try a more optimize algorithm
    def findMode(self, root: TreeNode) -> List[int]:
        lastSeenNode = None
        curCnt = 0
        maxCnt = 0
        lst = []
        # inorder traversal
        def rec(root) -> None:
            nonlocal lastSeenNode,curCnt,maxCnt,lst
            if not root: return
            rec(root.left)
            
            # make sure we're up to date with the most recently seen node's value
            if not lastSeenNode or lastSeenNode.val != root.val:
                curCnt = 1
                lastSeenNode = root
            else:
                curCnt+=1
                
            # at this point, there might be multiple modes
            if curCnt >= maxCnt:
                
                # if this if check is true, then we know our current value is the mode
                # and all previous modes should be cleared
                if curCnt > maxCnt:
                    maxCnt = curCnt
                    lst.clear()
                    lst.append(root.val)
                else:
                    lst.append(root.val)
            rec(root.right)
        rec(root)
        return lst
        
        
        
        