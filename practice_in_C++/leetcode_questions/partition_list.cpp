
#include "../templates/template.h"
#include "../data_structures/ListNode.h"

class Solution
{
private:
    void printll(ListNode* h)
    {
        while (h)
        {
            cout<<h->val<<' ';
            h=h->next;
        }
        nl;
    }

public:
    ListNode* partition(ListNode* head, int x)
    {
        ListNode* a = new ListNode(), *b = new ListNode();
        auto tmp = head;
        auto aApp = a, bApp = b;
        while (tmp)
        {
            int val = tmp->val;
            if (val < x)
            {
                aApp->next = tmp;
                aApp = aApp->next;
            }
            else
            {
                bApp->next = tmp;
                bApp = bApp->next;
            }
            tmp = tmp->next;
        }
        bApp->next = null;
        aApp->next = b->next;
        printll(head);

        tmp = a->next;
        delete a;
        delete b;

        return tmp;

    }
};


















/* brute force
vector<int> lessThans, greaterThans;
        // p(lessThans);
        // nl;
        // p(greaterThans);
        // nl;
        // lessThans.insert(lessThans.end(),all(greaterThans));
        // p(lessThans);
        auto tmp = head;
        while (tmp != null)
        {
            if (tmp->val < x)
                lessThans.emplace_back(tmp->val);
            else
                greaterThans.emplace_back(tmp->val);
        }

        lessThans.insert(lessThans.end(),all(greaterThans));

        tmp = head;
        for (auto val : lessThans)
        {
            tmp->val = val;
            tmp = tmp->next;
        }

        return head;
*/