using System.Collections.Generic;
using data_structures;

namespace practice_problems
{
    using ListNode = ListNode<int>;
    class MergeKSortedLists
    {
        public ListNode MergeKLists(ListNode[] lists)
        {
            if (lists.Length == 0)
                return null;

            // default is a maxheap, so change to min heap with greater<int>
            var minheap = new SortedList<int, int>();

            foreach (var lst in lists)
            {
                ListNode aux = lst;
                while (aux != null)
                {
                    minheap[aux.val] = minheap.ContainsKey(aux.val) ? minheap[aux.val] + 1 : 1;
                    aux = aux.next;
                }
            }

            // foreach (var kvp in minheap)
            // {
            //     Console.WriteLine($"{kvp.Key} : {kvp.Value}");
            // }

            ListNode dummy = new ListNode(0);
            ListNode tmp = dummy;
            ListNode last = null;

            foreach (var lst in lists)
            {
                if (lst != null)
                {
                    tmp.next = lst;
                    tmp = tmp.next;
                    break;
                }
            }

            foreach (var lst in lists)
            {
                if (lst == null)
                {
                    continue;
                }

                tmp = lst;

                // initially, last will be null
                if (last != null)
                {
                    last.next = tmp;
                }

                while (tmp != null)
                {
                    tmp.val = minheap.Keys[0];
                    if (--minheap[minheap.Keys[0]] <= 0)
                    {
                        minheap.RemoveAt(0);
                    }

                    last = tmp;
                    tmp = tmp.next;
                }
            }

            dummy = dummy.next;

            return dummy;
        }
    }

}




