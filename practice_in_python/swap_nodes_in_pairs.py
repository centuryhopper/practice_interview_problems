# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Slow solution
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        p1, p2, p3, nextRef = head, head.next, head, head.next.next
        retVal = p2

        if not nextRef:
            p2.next = head
            head.next = None
            return p2

        if not nextRef.next:
            p2.next = p1
            p1.next = nextRef
            return p2

        while nextRef and nextRef.next:

            nextRef = p2.next
            p2.next = p1
            p3 = p1
            p1 = nextRef if nextRef else p1

            # null check
            # p3.next = p2
            p2 = nextRef.next if nextRef else p2
            nextRef = p2.next if p2 else None
            p3.next = p2 if p2 else p1
            p3 = p1
            if p2:
                p2.next = p1
            # p3 = p1
            p1 = nextRef if nextRef else p1
            p2 = nextRef.next if nextRef else p2
            if (p2 and p3.next != p2):
                p3.next = p2
            else:
                p3.next = nextRef

        return retVal