from data_structures import TreeNode




# unoptimized iterative
# class Solution:

#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         d = {val:i for i,val in enumerate(inorder)}
#         root = TreeNode(preorder[0])
#         for i in range(1,len(preorder)):
#             tmp = root
#             val = preorder[i]
#             while True:
#                 if d[val] < d[tmp.val]:
#                     if not tmp.left:
#                         tmp.left = TreeNode(val)
#                         break
#                     else:
#                         tmp = tmp.left
#                 elif d[val] > d[tmp.val]:
#                     if not tmp.right:
#                         tmp.right = TreeNode(val)
#                         break
#                     else:
#                         tmp = tmp.right

#         return root



# unoptimized recursion
# class Solution:

#     def __init__(self):
#         self.d = None

#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         def rec(root, val) -> None:
#             if not root:
#                 return
#             # check in the in order realm for which direction to traverse to
#             if self.d[val] < self.d[root.val]:
#                 if not root.left:
#                     root.left = TreeNode(val)
#                 else:
#                     rec(root.left, val)
#             elif self.d[val] > self.d[root.val]:
#                 if not root.right:
#                     root.right = TreeNode(val)
#                 else:
#                     rec(root.right, val)
#         self.d = {val: i for i, val in enumerate(inorder)}
#         root = TreeNode(preorder[0])
#         for i in range(1, len(preorder)):
#             rec(root, preorder[i])

#         return root

# optimized recursion found online
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         hashMap = {}
#         for idx, val in enumerate(inorder):
#             hashMap[val] = idx
#         preorder_index = 0

#         def array_to_tree(left, right):
#             nonlocal preorder_index
#             if left > right: return None
#             root_value = preorder[preorder_index]
#             root = TreeNode(root_value)
#             preorder_index += 1
#             root.left = array_to_tree(left, hashMap[root_value] - 1)
#             root.right = array_to_tree(hashMap[root_value] + 1, right)

#             return root
#         return array_to_tree(0, len(preorder) - 1)