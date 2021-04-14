from data_structures.RandNode import RandNode

class Solution:
    def copyRandomList(self, head: RandNode) -> RandNode:
        if not head:
            return None

        # loop once to create a copy of each node
        # interweave them
        tmp = head
        while tmp:
            new = RandNode(x=tmp.val, next=tmp.next, random=tmp.random)
            tmp.next = new
            # print((tmp.val, new.val), end=' ')
            tmp = tmp.next.next

        # second loop will be for adjusting each copied node's next and random
        # pointers we know that each copy of the node is pointed to by the original node's
        # next pointer, which makes finding it for our random pointer much simpler
        tmp = head
        retVal = None
        i = 0
        while tmp:
            newTmp = tmp.next
            newTmp.random = newTmp.random.next if newTmp.random else None
            tmp = tmp.next.next
            if i == 0:
                retVal = newTmp
            newTmp.next = newTmp.next.next if newTmp.next else None
            i += 1

        tmp = retVal
        while tmp:
            print((tmp.val, tmp.random.val if tmp.random else ''), end=' ')
            tmp = tmp.next

        return None



'''
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None

        # loop once to create a copy of each node
        # interweave them
        tmp = head
        while tmp:
            new = Node(x=tmp.val,next=tmp.next,random=tmp.random)
            tmp.next = new
            print((tmp.val, new.val, tmp.random.val if tmp.random else ''), end=' ')
            tmp = tmp.next.next


        print()
        # second loop will be for adjusting each copied node's next and random
        # pointers we know that each copy of the node is pointed to by the original node's
        # next pointer, which makes finding it for our random pointer much simpler
        tmp = head
        retVal = None
        i = 0
        while tmp:
            newTmp = tmp.next
            newTmp.random = newTmp.random.next if newTmp.random else None
            tmp = tmp.next.next
            if i == 0: retVal = newTmp
            newTmp.next = newTmp.next.next if newTmp.next else None
            i += 1

        tmp = retVal
        while tmp:
            print((tmp.val, tmp.random.val if tmp.random else ''), end=' ')
            tmp = tmp.next

        return retVal
'''

