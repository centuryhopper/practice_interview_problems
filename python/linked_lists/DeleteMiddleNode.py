# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # assumes a non null head
        if not head.next:
            return None
        slow = fast = head
        prev = ListNode(-1,head)
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # slow should now be the middle node
        # and prev should now be the node right before where slow is
        # therefore rewire the link to remove the middle node
        prev.next = slow.next
        return head
        
