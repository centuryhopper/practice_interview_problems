# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.inorderLst = []
        self.iterator = -1
        self.inorder(root)

    def inorder(self, root: TreeNode) -> None:
        if not root: return
        self.inorder(root.left)
        self.inorderLst.append(root.val)
        self.inorder(root.right)

    def next(self) -> int:
        self.iterator += 1
        return self.inorderLst[self.iterator]

    def hasNext(self) -> bool:
        print(self.iterator)
        return self.iterator + 1 < len(self.inorderLst)



# def __init__(self, root: TreeNode):
#         self.stack = []
#         self.inOrder(root)

#     def inOrder(self, root):
#         if(root.right):
#             self.inOrder(root.right)
#         self.stack.append(root)
#         if(root.left):
#             self.inOrder(root.left)

#     def next(self) -> int:
#         while(self.hasNext()):
#             return self.stack.pop().val


#     def hasNext(self) -> bool:
#         return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()