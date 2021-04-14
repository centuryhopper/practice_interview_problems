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
        int sum = 0;
        void helper(TreeNode* root)
        {
            if (root == NULL) { return; }


// postorder traversal: Left, Right, Middle
                        //             left traversal
            helper(root->left);

//             right traversal
            helper(root->right);



            int l = 0, r = 0;

//             guarantee a value
            if (root->left != NULL)
            {
                l = root->left->val;
                root->val += l;
            }

            // guarantee a value
            if (root->right != NULL)
            {
                r = root->right->val;
                root->val += r;
            }

            sum += abs(l - r);

        }
    public:
        int findTilt(TreeNode* root)
        {
            helper(root);
            return sum;
        }
};