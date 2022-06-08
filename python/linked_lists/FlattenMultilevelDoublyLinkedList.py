"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    '''
    [4,7]
    1<=>2<=>3<=>7<=>8<=>11<=>12<=>9<=>10
    '''
    def flatten(self, head: 'Node') -> 'Node':
        '''
        iterative DFS approach
        '''
        if not head: return None
        # will hold a list of references
        # for re-linking later
        tmp = head
        stack = [tmp]
        while stack:
            cur = stack.pop()
            if cur.next: stack.append(cur.next)
            if cur.child:
                cur.next = cur.child
                cur.child.prev = cur
                stack.append(cur.child)
            if not cur.child and not cur.next:
                if stack:
                    stack[-1].prev = cur
                    cur.next = stack[-1]
            # sever the child pointers
            cur.child = None
        # tmp = tail = head
        # while tmp:
        #     print(tmp.val,end=' ')
        #     tmp=tmp.next
        # print()
        # while tail.next:
        #     tail=tail.next
        # while tail:
        #     print(tail.val,end=' ')
        #     tail = tail.prev

        return head


