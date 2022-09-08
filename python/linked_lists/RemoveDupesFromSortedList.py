# leetcode 83 Remove Duplicates from Sorted List

# Definition for singly-linked list.0
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = head
        tmp = head.next
        seen = set([prev.val])
        while tmp:
            if tmp.val in seen:
                # relink
                prev.next = tmp.next
                tmp = tmp.next
            else:
                seen.add(tmp.val)
                prev = prev.next
                tmp = tmp.next
        return head
            
        
