/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
#include <bits/stdc++.h>
#include "ListNode.h"




class Solution
{
    /*
    [9,9,9,9,9,9,9]
    [9,9,9,9]
     8 9 9 9 0 0 0 1
    */
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
    {
        // check edge cases
        auto node = new ListNode(-1);
        auto tmp = node;
        int carryOver = 0;
        auto a = l1, b = l2;

        while (a != nullptr || b != nullptr)
        {
            if (a != nullptr && b != nullptr)
            {
                int res = a->val + b->val + carryOver;

                tmp->next = new ListNode(res % 10);
                tmp = tmp->next;
                carryOver = res / 10;
                a = a->next;
                b = b->next;
                // cout<< res << ", " << carryOver << "\n";
            }
            else if (a == nullptr)
            {
                int res = b->val + carryOver;
                tmp->next = new ListNode(res % 10);
                tmp = tmp->next;
                carryOver = res / 10;
                b = b->next;
            }
            else if (b == nullptr)
            {
                int res = a->val + carryOver;
                tmp->next = new ListNode(res % 10);
                tmp = tmp->next;
                carryOver = res / 10;
                a = a->next;
            }
        }

        if (carryOver == 1) tmp->next = new ListNode(1);

        return node->next;



    }
};