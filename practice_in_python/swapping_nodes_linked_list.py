from data_structures import ListNode

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        lst = []
        # linked list to array
        while head:
            lst.append(head.val)
            head = head.next
        n = len(lst)
        lst[k-1], lst[n-k] = lst[n-k], lst[k-1]
        ret = ListNode(lst[0])
        tmp = ret
        # array back to linked list
        for i in range(1, n):
            new = ListNode(lst[i])
            tmp.next = new
            tmp = tmp.next
        return ret












# clever online solution O(1) space
# class Solution:
#     def swapNodes(self, head: ListNode, k: int) -> ListNode:
#         dummy = ListNode(0)
#         dummy.next = head
#         cur_node = head


#         for i in range(k - 1): #2
#             cur_node = cur_node.next

#         left_node = cur_node
#         right_node = head

#         while cur_node.next:
#             cur_node = cur_node.next
#             right_node = right_node.next

#         left_node.val, right_node.val = right_node.val, left_node.val
#         return dummy.next