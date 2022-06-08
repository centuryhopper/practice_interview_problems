# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from data_structures import ListNode
from types import Optional

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        use merge sort
        '''
        if not head or not head.next: return head

        def findMiddle(head):
            '''
            find the node right before the mid point of the list
            '''
            if not head: return None
            retVal = head
            slow = fast = head
            while fast and fast.next:
                retVal = slow
                slow = slow.next
                fast = fast.next.next
            return retVal

        def mergeTwoSortedList(head1, head2):
            '''
            this function assumes both lists are sorted
            '''
            if not head1: return head2
            if not head2: return head1

            dum = ListNode(-2**31)
            traverse = dum
            t1 = head1
            t2 = head2
            while t1 or t2:
                if t1 and t2:
                    if t1.val < t2.val:
                        traverse.next = t1
                        traverse = traverse.next
                        t1 = t1.next
                    else:
                        traverse.next = t2
                        traverse = traverse.next
                        t2 = t2.next
                elif t1:
                    traverse.next = t1
                    break
                elif t2:
                    traverse.next = t2
                    break
            return dum.next

        prevMid = findMiddle(head)
        # get a reference to the second half of the list
        head2 = prevMid.next
        # divide the list in half and make the calls
        prevMid.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(head2)

        # mergey merge
        ans = mergeTwoSortedList(l1,l2)

        return ans






