# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def iterative(head) -> ListNode:
            if not head:
                return head
            t1 = None
            t2 = head
            t3 = head.next
            while t3:
                t2.next = t1
                t1 = t2
                t2 = t3
                t3 = t3.next
            t2.next = t1
            return t2

        def rec(p, c, n) -> ListNode:
            if not c:
                return c
            if not n:
                c.next = p
                return c
            c.next = p
            return rec(c, n, n.next)
        # return rec(None,head,None if not head else head.next)
        # return iterative(head)
