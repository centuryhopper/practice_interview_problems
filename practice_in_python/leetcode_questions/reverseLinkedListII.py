# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head

        def printll(head):
            while head:
                print(head.val, end=' ')
                head = head.next
            print()

        ls = rs = head
        lh = None
        # get to correct position
        for _ in range(0, left-1):
            lh = ls
            ls = ls.next

        for _ in range(1, right+1):
            rs = rs.next
        # print(ls.val, '' if not rs else rs.val)

        # lh is left half of list thats not reversed (could be null)
        # rs is the right half of list that's not reversed
        # t1 = t2 = t3 = None
        t1 = None
        t2 = ls
        t3 = ls.next

        # cut off left side
        if lh:
            lh.next = None
        l = left
        while left < right:
            # print(t2.val)
            t2.next = t1
            t1 = t2
            t2 = t3
            t3 = None if not t3 else t3.next
            left += 1
        if t2:
            t2.next = t1

        # print(t1.val,t2.val,t3.val)
        if lh:
            lh.next = t2
            # print(lh.val)
        # linking left half with reversed section
        # if ls != head:
        ls.next = rs

        if l < 2:
            # print('t2:')
            return t2

        return head
