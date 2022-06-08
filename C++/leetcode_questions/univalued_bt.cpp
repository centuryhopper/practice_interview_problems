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
class Solution
{
    private:
        int rootVal;
        bool retVal = true;
        bool traverser(TreeNode* root)
        {
//             base case
            if (root->left == NULL && root->right == NULL)
            {
                return rootVal == root->val;
            }

//             AND check left and right children
            if (root->left != NULL)
            {
                retVal &= traverser(root->left);
            }

            if (root->right != NULL)
            {
                retVal &= traverser(root->right);
            }

//             AND check its own data
            retVal &= (root->val == rootVal);

            return retVal;
        }

    public:
        bool isUnivalTree(TreeNode* root)
        {
//             empty tree is assumed to be true
            if (root == NULL)
            {
                return true;
            }

//             use the root value to be a base
//             for what's correct and what's not
            rootVal = root->val;
            return traverser(root);
        }
};