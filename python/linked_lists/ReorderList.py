# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        tmp = head
        while tmp:
            stack.append(tmp)
            tmp = tmp.next
        tmp = head
        n = len(stack)
        compare = n // 2 if n % 2 == 0 else (n//2) + 1
        while len(stack) > compare:
            tmp2 = tmp.next
            tail = stack.pop()
            tmp.next = tail
            tail.next = tmp2
            tmp = tmp2
        tmp.next = None
        # tmp = head
        # while tmp:
        #     print(tmp.val,end=' ')
        #     tmp=tmp.next
