#include "./data_structures/ListNode.h"
#include <memory>
#include <queue>
#include <iostream>
#define null NULL
#define p(x) std::cout << x << std::endl;
#define ll long long
#define ar std::array
using namespace std;

class Solution
{
public:
    //  store all values in each linked list in a min heap then store in
    //  either a new linked list or try to reuse the old ones in the list.
    //  Because the constraint states that the list max size is 10^4 but any
    //  individual linked list can have a max size of 500, it is clear that
    //  it is better to process each individual linked list first for my algorithm.
    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        if (lists.size() == 0)
            return null;

        // default is a maxheap, so change to min heap with greater<int>
        priority_queue<int, vector<int>, greater<int>> minheap;

        for (auto &lst : lists)
        {
            ListNode *tmp = lst;
            while (tmp != null)
            {
                minheap.emplace(tmp->val);
                tmp = tmp->next;
            }
        }

        // while (!minheap.empty())
        // {
        //     p(minheap.top());
        //     minheap.pop();
        // }

        ListNode *dummy = new ListNode(10001);
        ListNode *tmp = dummy;
        ListNode *last = null;

        for (auto &lst : lists)
        {
            if (lst != null)
            {
                tmp->next = lst;
                tmp = tmp->next;
                break;
            }
        }

        for (auto &lst : lists)
        {
            if (lst == null)
            {
                continue;
            }

            tmp = lst;

            // initially, last will be null
            if (last != null)
            {
                last->next = tmp;
            }

            while (tmp != null)
            {
                tmp->val = minheap.top();
                p(minheap.top())
                minheap.pop();
                last = tmp;
                tmp = tmp->next;
            }
        }

        ListNode *toDelete = dummy;
        dummy = dummy->next;
        delete toDelete;

        return dummy;
    }
};