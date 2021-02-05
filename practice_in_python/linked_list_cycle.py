from data_structures import ListNode as l
class Solution:

    def hasCycle(self, head: l.ListNode) -> bool:
        # empty linked list or we reach the end
        if not head: return False
        # cycle detected
        if head.val == float('inf'): return True
        # mark as visited
        head.val = float('inf')

        return self.hasCycle(head.next)