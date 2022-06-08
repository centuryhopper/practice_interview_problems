from data_structures import ListNode

#region most recent solution
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # get length of list
        tmp = head
        cnt = 0
        while tmp:
            cnt+=1
            tmp=tmp.next
        if cnt == 1: return None
        desiredDist = cnt - n - 1
        if desiredDist < 0: return head.next
        tmp = head
        for _ in range(desiredDist):
            tmp = tmp.next
        tmp.next = tmp.next.next
        return head
#endregion


# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         dummy_head = ListNode()
#         dummy_head.next = head
#         tmp, delayedTmp = head, head
#         pred = dummy_head
#         while tmp:
#             # print(n)
#             if n <= 0:
#                 pred = delayedTmp
#                 # print(delayedTmp.val)
#                 delayedTmp = delayedTmp.next
#             tmp = tmp.next
#             n-=1
#         pred.next = delayedTmp.next
#         return dummy_head.next










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