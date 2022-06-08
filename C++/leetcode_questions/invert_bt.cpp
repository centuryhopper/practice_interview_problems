/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

#define null NULL

class Solution
{
    public:
        TreeNode* invertTree(TreeNode* root)
        {
//             null check
            if (root == null) { return null; }

            // traverse all the way to the left and right
            TreeNode* left = invertTree(root->left);
            TreeNode* right = invertTree(root->right);

            root->left = right;
            root->right = left;

            return root;
        }
};