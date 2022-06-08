# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from data_structures import ListNode

class Solution:
    
    '''
    1->2->3->2->1->null
    
    '''
    
    def isPalindrome(self, head: ListNode) -> bool:
        def reverseLst(head) -> ListNode:
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
        
        if not head.next: return True
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        secondHalf = None
        # length is odd
        if fast:
            secondHalf = slow.next
        # length is even
        else:
            secondHalf = slow
        # reverse the second half
        secondHalf = reverseLst(secondHalf)
        # sever the linked list
        slow.next = None
        
        
        while secondHalf and head:
            if head.val != secondHalf.val:
                return False
            head = head.next
            secondHalf = secondHalf.next
        return True
            
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            