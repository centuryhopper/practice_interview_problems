// /**
//  * Definition for singly-linked list.
//  * public class ListNode {
//  *     public int val;
//  *     public ListNode next;
//  *     public ListNode(int val=0, ListNode next=null) {
//  *         this.val = val;
//  *         this.next = next;
//  *     }
//  * }
//  */
// public class MergeTwoSortedLinkedLists
// {
//     public ListNode mergeTwoSortedLinkedLists(ListNode l1, ListNode l2)
//     {
//         if (l1 == null) { return l2; }
//         if (l2 == null) { return l1; }

//         if (l1.next == null)
//         {
//             if (l1.val <= l2.val)
//             {
//                 l1.next = l2;
//                 return l1;
//             }
//         }
//         if (l2.next == null)
//         {
//             if (l2.val <= l1.val)
//             {
//                 l2.next = l1;
//                 return l2;
//             }
//         }

//         ListNode ret = new ListNode(), tmp = null;

//         // initialize
//         if (l1.val <= l2.val)
//         {
//             ret.next = l1;
//             l1 = l1.next;
//             tmp = ret.next;
//         }
//         else
//         {
//             ret.next = l2;
//             l2 = l2.next;
//             tmp = ret.next;
//         }



//         while (l1 != null || l2 != null)
//         {
//             if (l1 != null)
//             {
//                 if (l1.val <= l2.val)
//                 {
//                     tmp.next = l1;
//                     l1 = l1.next;
//                     tmp = tmp.next;
//                 }
//             }

//             if (l1 == null)
//             {
//                 // link tmp with rest of l2
//                 tmp.next = l2;
//                 break;
//             }

//             if (l2 != null)
//             {
//                 if (l2.val < l1.val)
//                 {
//                     tmp.next = l2;
//                     l2 = l2.next;
//                     tmp = tmp.next;
//                 }
//             }

//             if (l2 == null)
//             {
//                 // link tmp with rest of l1
//                 tmp.next = l1;
//                 break;
//             }
//         }

//         ret = ret.next;

//         return ret;



//     }
// }