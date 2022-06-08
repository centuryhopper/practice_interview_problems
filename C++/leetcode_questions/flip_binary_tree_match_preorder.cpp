
#include <vector>
#include "../data_structures/TreeNode.h"
#define null NULL
#define p(x) std::cout << x << "\n";
using namespace std;
class Solution
{

private:
// global var i
    int i = 0;
    // true for success, false for failure
    bool preorder(TreeNode* root, vector<int>& toSwap, vector<int>& voyage)
    {
        if (root == nullptr) return true;

        // if they are different,
        // add root val to the list
        // and traverse the right subtree
        // then left subtree
        if (root->val != voyage[i])
        {
            return false;
        }

        ++i;
        // check left val and add to swap list if left val != voyage[i]
        // and also traverse right subtree first, then left
        // otherwise if left val == voyage[i]
        // perform regular preorder traversal by exploring left first,
        // then right
        if (root->left != nullptr && root->left->val != voyage[i])
        {
            toSwap.emplace_back(root->val);
            return preorder(root->right, toSwap, voyage) && preorder(root->left, toSwap, voyage);
        }

        return preorder(root->left, toSwap, voyage) && preorder(root->right, toSwap, voyage);
    }

public:
    vector<int> flipMatchVoyage(TreeNode* root, vector<int>& voyage)
    {
        vector<int> lst;
        bool res = preorder(root, lst, voyage);

        return res ? lst : vector{-1};
    }
};

