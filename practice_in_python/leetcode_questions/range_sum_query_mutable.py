

class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None
        self.sum = 0


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.root = self.buildSegmentTree(0, len(nums)-1)

    # time: O(n)
    def buildSegmentTree(self, start, end) -> SegmentTreeNode:
        # out of bounds case
        if start > end:
            return None
        node = SegmentTreeNode(start, end)
        # leaf node case
        if start == end:
            node.sum = self.nums[start]
            return node
        mid = int(start + (end - start) / 2)
        node.left = self.buildSegmentTree(start, mid)
        node.right = self.buildSegmentTree(mid+1, end)
        node.sum = node.left.sum + node.right.sum
        return node

    # find the leaf node to update
    # time: O(log n)
    def updateHelper(self, root, i, val) -> None:
        # if the start and end are same, then we
        # found our leaf node
        if root.start == root.end:
            root.sum = val
            return
        # recurse left or right depending on the i value
        mid = root.start + int((root.end - root.start) / 2)
        # go left
        if i <= mid:
            self.updateHelper(root.left, i, val)
        # go right
        else:
            self.updateHelper(root.right, i, val)
        root.sum = root.left.sum + root.right.sum

    def sumRangeHelper(self, root, start, end) -> int:
        # found the node with matching start and end values
        if root.start == start and root.end == end:
            return root.sum
        mid = root.start + int((root.end - root.start) / 2)
        if end <= mid:
            return self.sumRangeHelper(root.left, start, end)
        if start > mid:
            return self.sumRangeHelper(root.right, start, end)
        return self.sumRangeHelper(root.left, start, mid) + self.sumRangeHelper(root.right, mid+1, end)

    def update(self, index: int, val: int) -> None:
        self.updateHelper(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.sumRangeHelper(self.root, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


# region brute force TLE
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sumAr = []
        runningSum = 0
        for num in nums:
            runningSum += num
            self.sumAr.append(runningSum)
        print(self.sumAr)

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        runningSum = 0
        for i, num in enumerate(self.nums):
            runningSum += num
            self.sumAr[i] = runningSum

    def sumRange(self, left: int, right: int) -> int:
        if right == left:
            return self.nums[right]
        if left == 0:
            return self.sumAr[right]
        return self.sumAr[right] - self.sumAr[left - 1]
# endregion
