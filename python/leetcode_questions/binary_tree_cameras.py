from data_structures import TreeNode

class Solution:
    def __init__(self):
        self.cams = 0
        # stores all the TreeNodes that have a camera
        self.st = None
    # start from bottom and work your way up when filling which nodes with cameras
    # never put a camera at the lowest levels unless we just have a tree with a single node
    # DO A POSTORDER TRAVERAL
    def f(self, root, parent) -> None:
        if not root: return
        self.f(root.left, root)
        self.f(root.right, root)
        # if parent is null and current node doesn't have camera
        # OR if either its left or right child are not covered,
        # then add a camera to this current node
        if (not parent and root not in self.st) or (root.left not in self.st or root.right not in self.st):
            self.cams+=1
            # now its parent, itself, and children are covered
            self.st.update({parent, root, root.left, root.right})
    def minCameraCover(self, root: TreeNode) -> int:
        # empty tree case
        if not root: return 0
        # make sure leaf nodes don't get a camera added to them
        self.st = {None}
        self.f(root, None)
        return self.cams
























'''
failed attempt

class Solution:

    # distance: The distance since camera was last taken
    def f(self, root, parentHasCamera, distance) -> int:
        if not root:
            return 0
        if parentHasCamera:
            # don't give your self a camera because your parent already has one
            return self.f(root.left, False, distance+1) + self.f(root.right, False, distance+1)

        if distance > 2:
            # Then must give your self a camera and reset distance
            return 1 + self.f(root.left, True, 1) + self.f(root.right, True, 1)

        # take camera and reset distance
        resWithCamera = 1 + self.f(root.left, True, 1) + self.f(root.right, True, 1)

        # dont take camera and continue the distance
        resWithOutCamera = self.f(root.left, False, distance+1) + self.f(root.right, False, distance+1)

        return min(resWithCamera,resWithOutCamera)


    def minCameraCover(self, root: TreeNode) -> int:

        # edge case of only a single tree node
        if not root.left and not root.right: return 1

        return min(self.f(root, False, 0), self.f(root, True, 1))


'''


