# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = 0
        tmp = head
        while tmp:
            n+=1
            tmp=tmp.next
        tmp = head
        ans = 0
        while tmp:
            ans += tmp.val << (n - 1)
            n-=1
            tmp=tmp.next
        return ans
    
    