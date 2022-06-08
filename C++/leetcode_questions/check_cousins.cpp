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
#define print(x) std::cout << x << std::endl;
using namespace std;


class Solution
{
//     approach:
//     -have a variable that keeps track of each node's
//     parent
//     -have a variable that keeps track of the current depth of each node
    int xParent = -2, yParent = -1;
    int xDepth = 0, yDepth = 0;
    bool foundX = false, foundY = false;


public:
    void GetDepthAndParent(TreeNode* root, int& parent, int number, int& depth, bool& found)
    {
        if (root->val == number) { found = true; return; }

        if (root->left != null && !found)
        {
            parent = root->val;
            depth += 1;
            GetDepthAndParent(root->left, parent, number, depth, found);
        }

        if (root->right != null && !found)
        {
            parent = root->val;
            depth += 1;
            GetDepthAndParent(root->right, parent, number, depth, found);
        }

        if (!found) { --depth; }
    }


    bool isCousins(TreeNode* root, int x, int y)
    {
        if (root == null) { return false; }

        if (root->val == x || root->val == y) { return false; }

//         find x's parent and depth of x
        GetDepthAndParent(root, xParent, x, xDepth, foundX);

//         find y's parent and depth of y
        GetDepthAndParent(root, yParent, y, yDepth, foundY);

        print("xParent: " + to_string(xParent));
        print("yParent: " + to_string(yParent));
        print("xDepth: " + to_string(xDepth));
        print("yDepth: " + to_string(yDepth));

        // compare and return the result
        return (xParent != yParent) && (xDepth == yDepth);
    }
};