class RandNode:
    '''Definition for a singly-linked list node with a pointer to a random node in the list'''
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random