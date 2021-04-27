from data_structures import ListNode
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode()
        dummy_head.next = head
        tmp, delayedTmp = head, head
        pred = dummy_head
        while tmp:
            # print(n)
            if n <= 0:
                pred = delayedTmp
                # print(delayedTmp.val)
                delayedTmp = delayedTmp.next
            tmp = tmp.next
            n-=1
        pred.next = delayedTmp.next
        return dummy_head.next










#interesting online recursive solution
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         def recursiveHelper(node):
#             if node == None:
#                 return 0
#             currentPos = recursiveHelper(node.next) + 1
#             if currentPos == n+1:
#                 node.next = node.next.next
#             return currentPos
#         dummyHead = ListNode(0, head)
#         recursiveHelper(dummyHead)
#         return dummyHead.next


# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         slow=fast=head

#         for i in range(n):
#             fast=fast.next
#         if fast is None:
#             return head.next
#         while fast and fast.next:
#             fast=fast.next
#             slow=slow.next
#         slow.next=slow.next.next
#         return head