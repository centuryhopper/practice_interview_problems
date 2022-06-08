from data_structures import TreeNode

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # postorder
        def treeTotalSum(root)->int:
            if not root: return 0
            l = treeTotalSum(root.left)
            r = treeTotalSum(root.right)
            root.val += (l + r)
            # print(root.val)
            return root.val
        totalSum = treeTotalSum(root)
        getMaxProd = 0
        mod = 7 + 10**9
        # print(totalSum)
        # inorder
        def rec(root)->None:
            nonlocal totalSum,getMaxProd
            if not root:return
            rec(root.left)
            getMaxProd = max(getMaxProd, (totalSum-root.val) * root.val)
            rec(root.right)
        rec(root)

        return getMaxProd % mod
