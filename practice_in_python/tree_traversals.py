from TreeNode import TreeNode
from collections import deque


def create_treenode(val, left:TreeNode=None, right:TreeNode=None) -> TreeNode:
    newNode = TreeNode(val, left, right)
    return newNode

# def recursive_generate(root: TreeNode, levels: int) -> None:
#     if levels <= 0: return
#     if not root.left: root.left = TreeNode()

def pre_order(root:TreeNode) -> None:
    if not root: return
    print(root.val, end=' ')
    pre_order(root.left)
    pre_order(root.right)

def in_order(root:TreeNode) -> None:

    if not root: return
    in_order(root.left)
    print(root.val, end=' ')
    in_order(root.right)

def post_order(root:TreeNode) -> None:
    if not root: return
    post_order(root.left)
    post_order(root.right)
    print(root.val, end=' ')

# prints all on one line
def level_order(root:TreeNode, d: deque[TreeNode]) -> None:
    if not root: return
    d.append(root)
    while d:
        item = d[0]
        d.popleft()
        print(item.val, end=' ')
        if item.left: d.append(item.left)
        if item.right: d.append(item.right)

def level_by_level(root: TreeNode, d: deque[TreeNode]) -> None:
    if not root: return
    d.append(root)
    d.append(None)
    while d:
        item = d[0]
        d.popleft()
        if not item:
            print()
            d.append(None)
            # no more node values to print, so we return out
            if len(d) == 1:break
        else:
            print(item.val, end=' ')
            if item.left: d.append(item.left)
            if item.right: d.append(item.right)





if __name__ == '__main__':

    root = create_treenode('a')
    root.left = create_treenode('b')
    root.right = create_treenode('c')
    root.left.left = create_treenode('d')
    root.left.right = create_treenode('e')
    root.right.left = create_treenode('f')
    root.right.right = create_treenode('g')
    root.left.left.left = create_treenode('h')
    root.left.left.right = create_treenode('i')
    root.right.left.left = create_treenode('j')
    root.right.left.right = create_treenode('k')
    root.right.right.right = create_treenode('l')

    # pre_order(root)
    # in_order(root)
    # post_order(root)

    # d = deque()
    # level_order(root, d)
    # level_by_level(root, d)

