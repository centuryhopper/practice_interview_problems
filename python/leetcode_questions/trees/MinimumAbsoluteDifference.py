from data_structures import TreeNode


class Solution:

    '''
                        236
                    /         \
                  104         701
                    \           \
                    227         911

    '''
    # use inorder traversal
    # assumes there are at least two nodes and that
    # all node values are [0,10^5]

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = float('inf')
        lastSeenNode = None
        def rec(root) -> None:
            nonlocal ans, lastSeenNode
            if not root:
                return
            l = rec(root.left)
            ans = min(ans, abs(lastSeenNode.val -
                      root.val if lastSeenNode else float('inf')))
            lastSeenNode = root
            # print(lastSeenNode.val)
            r = rec(root.right)
            return
        rec(root)
        return ans
