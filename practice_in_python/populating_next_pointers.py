
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def helper(root: 'Node') -> None:
            if not root:
                return
            p = root
            cH, c = None, None
            while p:
                if p.left:
                    if not cH:
                        cH = p.left
                    else:
                        c.next = p.left
                    c = p.left
                if p.right:
                    if not cH:
                        cH = p.right
                    else:
                        c.next = p.right
                    c = p.right
                p = p.next
            helper(cH)

        helper(root)
        return root
