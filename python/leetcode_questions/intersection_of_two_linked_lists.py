from data_structures.ListNode import ListNode


# my solution
class Solution:
    def getIntersectionNode(self, a: ListNode, b: ListNode) -> ListNode:

        # get length of both lists
        t1, t2 = a, b
        lenA, lenB = 0,0
        diff = 0
        while t1 or t2:
            if t1:
                lenA += 1
                t1 = t1.next
            if t2:
                lenB += 1
                t2 = t2.next

        # reset auxiliary pointers
        t1, t2 = a, b

        # move the ptr of the longer linked list ahead
        # diff times in order to match where the shorter
        # linked list starts
        if lenA > lenB:
            diff = lenA - lenB
            for _ in range(diff):
                t1 = t1.next
        elif lenB > lenA:
            diff = lenB - lenA
            for _ in range(diff):
                t2 = t2.next

        while t1:
            if t1 == t2:
                return t1
            t1 = t1.next
            t2 = t2.next

        # no intersection at this point
        return None



# more optimized solution found online
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

#         if not headA or not headB:
#             return None

#         pointA = headA
#         pointB = headB


#         while pointA != pointB:
#             pointA = pointA.next
#             pointB = pointB.next

#             if pointA == pointB:
#                 return pointA

#             if pointA is None:
#                 pointA = headB

#             if pointB is None:
#                 pointB = headA

#         return pointA