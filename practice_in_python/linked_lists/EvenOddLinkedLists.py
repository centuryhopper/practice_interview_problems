# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        tmp = head
        while tmp:
            n+=1
            tmp=tmp.next
        if n <= 2: return head
        # two pointers
        odd,even = head,head.next
        aux = even
        while even and even.next:
            odd.next = odd.next.next
            odd=odd.next
            even.next = even.next.next
            even=even.next

        odd.next = aux
        return head
