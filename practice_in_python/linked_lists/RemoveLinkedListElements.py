# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    '''
    [1,2,2,1]
    2

    '''
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # make sure head isn't referencing a
        # value to be deleted
        while head and head.val == val:
            head = head.next
        tmp = head
        while tmp and tmp.next:
            if tmp.next.val == val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return head




