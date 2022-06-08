#include <bits/stdc++.h>
#include "../data_structures/ListNode.h"
























#pragma region more optimized Solution
// class Solution {
//     ListNode* reverseList(ListNode* head) {
//         ListNode* prev=nullptr;
//         ListNode* curr=head;
//         while(curr) {
//             ListNode* next=curr->next;
//             curr->next=prev;
//             prev=curr;
//             curr=next;
//         }
//         return prev;
//     }
// public:
//     bool isPalindrome(ListNode* head) {
//         int n=0;
//         ListNode* iter=head;
//         while(iter) iter=iter->next, n++;
//         if(n<2) return true;
//         // printf("-->%d\n", n);
//         iter=head;
//         for(int i=1;i<n/2;++i) iter=iter->next;
//         ListNode* iter2 = (n%2) ? iter->next->next : iter->next;
//         iter->next=nullptr;
//         // printf("iter2->val=%d\n",xiter2->val);
//         iter=reverseList(head);
//         while(iter) {
//             if(iter->val!=iter2->val) return false;
//             iter=iter->next;
//             iter2=iter2->next;
//         }
//         return true;
//     }
// };
#pragma endregion