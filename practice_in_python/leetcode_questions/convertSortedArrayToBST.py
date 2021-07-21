from data_structures import TreeNode

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def bstInsert(root,val) -> TreeNode:
            if not root:
                return TreeNode(val)
            if val < root.val:
                root.left = bstInsert(root.left,val)
            elif val > root.val:
                root.right = bstInsert(root.right,val)
            # assume no duplicates
            return root
        def getMid(nums,lo,hi)->None:
            nonlocal root
            # find mid and insert into bst
            if lo > hi: return
            mid = (lo+hi)//2
            root = bstInsert(root,nums[mid])
            getMid(nums,lo,mid-1)
            getMid(nums,mid+1,hi)
        root = None
        getMid(nums,0,len(nums)-1)
        return root
        
            
            
            
        