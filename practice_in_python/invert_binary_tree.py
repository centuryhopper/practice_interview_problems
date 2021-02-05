from data_structures import TreeNode as t
'''
C++ solution:
    if (root == null) return null;

    TreeNode* tmpL = invertTree(root->left);

    root->left = invertTree(root->right);
    root->right = tmpL;

    return root;
'''
class Solution:
    def invertTree(self, root: t.TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = self.invertTree(
            root.right), self.invertTree(root.left)
        return root
