# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    [2,2,1]
    [2,null,2,null,2,null,1]

    '''
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def printll(head)->None:
            while head:
                print(head.val,end=' ')
                head=head.next
            print()
        def rec(head,root)->bool:
            # head reaching null is priority
            if not head: return True
            if not root: return False
            if head.val != root.val:
                return False
            return rec(head.next,root.left) or rec(head.next,root.right)
        # head reaching null is priority
        # if not head: return True
        if not root: return False

        if rec(head,root): return True
        # print(root.val)
        # printll(head)
        # check children
        return self.isSubPath(head,root.left) or self.isSubPath(head,root.right)

