using System;
using data_structures;

namespace practice_problems
{
    public class LinkedListRandomNode<T>
    {
        Random r;
        ListNode<T> cur;

        /** @param head The linked list's head.
            Note that the head is guaranteed to be not null, so it contains at least one node. */
        public LinkedListRandomNode(ListNode<T> head)
        {
            r = new Random();
            cur = head;
        }

        /** Returns a random node's value. */
        public T GetRandom()
        {
            double currentNodeCount = 1;
            dynamic res = 0;

            for (var tmp = cur; tmp != null; tmp = tmp.next)
            {
                if (r.NextDouble() < (1 / currentNodeCount))
                {
                    res = tmp.val;
                }
                ++currentNodeCount;
            }

            return res;
        }
    }
}