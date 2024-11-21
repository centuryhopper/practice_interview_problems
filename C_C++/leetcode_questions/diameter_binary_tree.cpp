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

#define print(x) std::cout << x << std::endl;
#define null NULL
#define fl(i, k, n) for (int i = k; i < n; ++i)

class Solution
{
    // depth-first search
    int findLongestPath(TreeNode* root)
    {
        if (root == null) { return 0; }

        int path = 1 + max(findLongestPath(root->left), findLongestPath(root->right));

        return path;
    }

public:
    int diameterOfBinaryTree(TreeNode* root)
    {
//         empty tree check
        if (root == null) { return 0; }

//         find longest path on the left subtree
        int lPath = findLongestPath(root->left);
//         find longest path on the right subtree
        int rPath = findLongestPath(root->right);

        int sum = lPath + rPath;

//         cache results to avoid more recursion
        int resL = diameterOfBinaryTree(root->left);
        int resR = diameterOfBinaryTree(root->right);

        if (resL > sum)
        {
            sum = resL;
        }

        if (resR > sum)
        {
            sum = resR;
        }
//         add them up
        return sum;
    }
};