from data_structures import TreeNode

class Solution:
    # in order traversal
    '''
    time: O(n) because we would traverse the entire tree in the case that the sum isn't found
    space:O(n) because we could in the worst case store all node values into our set in the case that the sum isn't found
    '''
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def rec(root,k,st) -> bool:
            if not root: return False
            l = rec(root.left,k,st)
            # print(root.val)
            # if we've seen the complement already then we're good to go
            if k - root.val in st: return True
            st.add(root.val)
            r = rec(root.right,k,st)
            return l or r
        return rec(root,k,set())
        
        
        