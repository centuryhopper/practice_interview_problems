# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cnt = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def rec(root, targetSum):
            if not root: return
            if targetSum == root.val:
                self.cnt +=1
            rec(root.left,targetSum-root.val)
            rec(root.right,targetSum-root.val)
        if not root: return 0
        rec(root,targetSum)
        self.pathSum(root.left,targetSum)
        self.pathSum(root.right,targetSum)
        return self.cnt


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d = collections.defaultdict(int)
        self.cnt = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def rec(root, curSum, targetSum):
            if not root: return
            curSum+=root.val
            # print(curSum,targetSum,self.d[curSum - targetSum])
            self.cnt+=self.d[curSum - targetSum]
            self.d[curSum]+=1
            rec(root.left,curSum,targetSum)
            rec(root.right,curSum,targetSum)
            # current branch is finished procesing so, decremented it to avoid repeated counts
            self.d[curSum]-=1
            return
        self.d[self.cnt]+=1
        rec(root,0,targetSum)
        # print(self.d)
        return self.cnt
