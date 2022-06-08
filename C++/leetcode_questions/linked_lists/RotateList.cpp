#include <bits/stdc++.h>
#include "ListNode.h"

class Solution
{

    /*
    1,2,3,4,5
    p1      p2
    æ
    5,1,2,3,4
    p1      p2

    4,5,1,2,3

    */
public:
    ListNode* rotateRight(ListNode* head, int k)
    {
        if (head == nullptr || head->next == nullptr) return head;
        /* brute force (TLE)
        ListNode* p1 = head, *p2 = head;
        for (int i = 0;i < k;i++)
        {
            auto prev = head;
            while (p2->next != nullptr)
            {
                prev = p2;
                p2=p2->next;
            }
            prev->next = nullptr;
            p2->next = head;

            head = p2;
        }

        return head;*/

        int size = 0;
        ListNode* tmp = head;
        auto tail = tmp;
        while (tmp != nullptr)
        {
            tail = tmp;
            tmp=tmp->next;
            size++;
        }
        // make sure we don't out of bounds
        int goal = k % size;
        if (goal == 0) return head;
        tmp = head;
        auto prev = head;
        while (size-- > goal)
        {
            prev = tmp;
            tmp = tmp->next;
        }

        // rewiring
        prev->next = nullptr;
        tail->next = head;
        head = tmp;

        return head;



    }
};




















