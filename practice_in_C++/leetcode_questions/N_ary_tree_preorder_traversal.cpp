#include "templates/template.h"


/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/


class Solution
{
public:

    // no recursion. Only iterative
    vector<int> preorder(Node* root)
    {
        if (!root) return {};
        stack<Node*> st({root});
        vector<int> v;

        while (!st.empty())
        {
            auto node = st.top();
            v.emplace_back(node->val);
            st.pop();
            auto kids = node->children;
            for (auto it = kids.rbegin(); it != kids.rend();++it)
            {
                st.push(*it);
            }
        }
        // p(v);

        return v;

    }
};


