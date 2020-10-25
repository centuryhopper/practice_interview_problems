#include <cstdint>
#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <climits>
#include <iterator>
#include <array>
#include <vector>
#include <map>
#include <set>
#include <tuple>
#include <stack>
#include <queue>
#define print(x) std::cout << x << std::endl;
#define fl(i, k, n) for (int i = k; i < n; ++i)
#define null NULL
using namespace std;

//   Definition for a binary tree node.
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#define null NULL
class Solution
{
    public:
        int maxDepth(TreeNode *root)
        {
            if (root == null)
            {
                return 0;
            }

            // each existing node will count as
            //             a depth level
            int leftCount = 1, rightCount = 1;

            // traverse left and right
            //             and take the max
            leftCount += maxDepth(root->left);
            rightCount += maxDepth(root->right);

            return max(leftCount, rightCount);
        }
};