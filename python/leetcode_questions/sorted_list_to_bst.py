from data_structures import TreeNode, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root:TreeNode) -> None:
        if not root: return
        self.inorder(root.left)
        print(root.val, end=' ')
        self.inorder(root.right)

    def bstInsert(self, root: TreeNode, node:TreeNode) -> TreeNode:
        # found an opening to insert the node
        if not root: return node
        if node.val < root.val:
            # go left
            root.left = self.bstInsert(root.left, node)
        elif node.val > root.val:
            # go right
            root.right = self.bstInsert(root.right, node)
        # we do not allow duplicates in a BST
        return root

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        fast = head
        mid = head
        cut = None
        # get mid point in the list
        while fast and fast.next:
            cut = mid
            mid = mid.next
            fast = fast.next.next

        # cut the linked list in half for the recursive calls
        # very crucial step
        if cut: cut.next = None

        root = TreeNode(mid.val)

        # linked list with one node base case
        if head == mid: return root
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root




        
















# class Solution:
#     def inorder(self, root:TreeNode) -> None:
#         if not root: return
#         self.inorder(root.left)
#         print(root.val, end=' ')
#         self.inorder(root.right)

#     def bstInsert(self, root: TreeNode, node:TreeNode) -> TreeNode:
#         # found an opening to insert the node
#         if not root: return node
#         if node.val < root.val:
#             # go left
#             root.left = self.bstInsert(root.left, node)
#         elif node.val > root.val:
#             # go right
#             root.right = self.bstInsert(root.right, node)
#         # we do not allow duplicates in a BST
#         return root

#     def sortedListToBST(self, head: ListNode) -> TreeNode:
#         if not head: return None
#         tmp = head
#         lst = []
#         while tmp:
#             lst.append(tmp.val)
#             tmp = tmp.next
#         # print(lst)

#         mid = len(lst) // 2
#         root = TreeNode(lst[mid])
#         i, j = mid - 1, mid + 1
#         while i >= 0 or j < len(lst):
#             if i >= 0:
#                 self.bstInsert(root, TreeNode(lst[i]))
#                 i -= 1
#             if j < len(lst):
#                 self.bstInsert(root, TreeNode(lst[j]))
#                 j += 1
#         # self.inorder(root)
#         return root



