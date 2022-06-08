# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    notes: in postorder traversal: root node is always processed last

    thought-process:
    build a hashmap of the inorder array to look up the index of each value when traversing the postorder array and how they're positions help determine where to insert the current value into the tree

    Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
    Output: [3,9,20,null,null,15,7]
    '''
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # build hashmap
        lookup = {val:i for i,val in enumerate(inorder)}
        root = TreeNode(postorder[-1])
        n = len(postorder)
        # we know the last number is the root node
        # val, so we skip it
        for i in range(n-2,-1,-1):
            tmp = root
            cur = postorder[i]
            while True:
                if lookup[cur] < lookup[tmp.val]:
                    if tmp.left:
                        tmp = tmp.left
                    else:
                        tmp.left = TreeNode(cur)
                        break
                elif lookup[cur] > lookup[tmp.val]:
                    if tmp.right:
                        tmp = tmp.right
                    else:
                        tmp.right = TreeNode(cur)
                        break
        return root









