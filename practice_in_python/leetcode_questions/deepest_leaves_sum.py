from data_structures import TreeNode

class Solution:
    def __getMaxDepth(self, root:TreeNode) -> int:
        if not root: return 0
        leftSubTree = 1 + self.__getMaxDepth(root.left)
        rightSubTree = 1 + self.__getMaxDepth(root.right)
        return max(leftSubTree, rightSubTree)

    def __getLeavesSum(self, root:TreeNode,cur:int, depth:int) -> int:
        if not root: return 0
        if cur == depth: return root.val
        acc = 0
        # check left and right subtrees
        acc += self.__getLeavesSum(root.left, cur+1, depth)
        acc += self.__getLeavesSum(root.right, cur+1, depth)
        return acc

    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root: return
        val = self.__getMaxDepth(root)
        # print(val)
        return self.__getLeavesSum(root, 1, val)


    # online optimized solution
    # def deepestLeavesSum(self, root: TreeNode) -> int:
    #     queue = [root]
    #     while(1):
    #         next_queue = list()
    #         for node in queue:
    #             if(node.left):
    #                 next_queue.append(node.left)
    #             if(node.right):
    #                 next_queue.append(node.right)
    #         if(next_queue):
    #             queue = next_queue
    #         else:
    #             return sum(map(lambda x:x.val,queue))