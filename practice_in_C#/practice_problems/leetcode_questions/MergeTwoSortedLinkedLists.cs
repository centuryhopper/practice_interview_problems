using data_structures;

namespace practice_problems
{
    using Node = ListNode<int>;
    public class MergeTwoSortedLinkedLists
    {
        private static Node GetMiddleNode(Node node)
        {
            Node dist = node, twice_dist = node;

            // regardless of the number of nodes,
            // dist will be at the middle node
            // when twice_dist is null or at the last node of the list
            while (twice_dist != null && twice_dist.next != null)
            {
                dist = dist.next;
                twice_dist = twice_dist.next.next;
            }

            return dist;
        }

        private static Node MergeTwoLists(Node l1, Node l2)
        {
            if (l1 == null) { return l2; }
            if (l2 == null) { return l1; }

            if (l1.next == null)
            {
                if (l1.val <= l2.val)
                {
                    l1.next = l2;
                    return l1;
                }
            }
            if (l2.next == null)
            {
                if (l2.val <= l1.val)
                {
                    l2.next = l1;
                    return l2;
                }
            }

            Node ret = null, tmp = null;

            // initialize
            if (l1.val <= l2.val)
            {
                ret = tmp = l1;
                l1 = l1.next;
            }
            else
            {
                ret = tmp = l2;
                l2 = l2.next;
            }



            while (true)
            {
                if (l1 != null)
                {
                    if (l1.val <= l2.val)
                    {
                        tmp.next = l1;
                        l1 = l1.next;
                        tmp = tmp.next;
                    }
                }

                if (l1 == null)
                {
                    // link tmp with rest of l2
                    tmp.next = l2;
                    break;
                }

                if (l2 != null)
                {
                    if (l2.val < l1.val)
                    {
                        tmp.next = l2;
                        l2 = l2.next;
                        tmp = tmp.next;
                    }
                }

                if (l2 == null)
                {
                    // link tmp with rest of l1
                    tmp.next = l1;
                    break;
                }
            }
            return ret;
        }

        public static void MergeSortLinkedList()
        {
            // head = MergeSortLinkedList(head);
        }

        private static Node MergeSortLinkedList(Node node)
        {
            // if input is empty or just a single node
            if (node == null || node.next == null) { return node; }

            // get middle node of linked list and its next node
            Node midNode = GetMiddleNode(node);
            Node midNodeNext = midNode.next;

            Node firstHalf = MergeSortLinkedList(node);
            Node secondHalf = MergeSortLinkedList(midNode);

            Node sortedList = MergeTwoLists(firstHalf, secondHalf);

            return sortedList;
        }
    }
}

