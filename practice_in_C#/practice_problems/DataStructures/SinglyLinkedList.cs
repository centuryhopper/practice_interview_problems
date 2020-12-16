using System;

namespace data_structures
{
    using Node = ListNode<int>;
    public class SinglyLinkedList
    {
        public Node head { get; private set; }
        public Node tail { get; private set; }

        public SinglyLinkedList(int val, Node next = null)
        {
            head = new Node(val, next);
            tail = head;
        }

        public void MergeSortLinkedList()
        {
            head = MergeSortLinkedList(head, tail);
        }

        public void TailInsert(int val)
        {
            Node newNode = new Node(val, null);
            tail.next = newNode;
            tail = newNode;
        }

        public void PrintList()
        {
            Node tmp = head;
            while (tmp != null)
            {
                System.Console.Write(string.Format("{0}{1}", tmp.val, tmp.next == null ? string.Empty : " "));
                tmp = tmp.next;
            }
            System.Console.WriteLine();
        }

        public Node GetMiddleNode(Node h, Node t = null)
        {
            Node dist = h, twice_dist = h;

            // regardless of the number of nodes,
            // dist will be at the middle node
            // when twice_dist is null or at the last node of the list
            while (twice_dist != t && twice_dist.next != t)
            {
                dist = dist.next;
                twice_dist = twice_dist.next.next;
            }

            return dist;
        }

        private Node MergeTwoLists(Node l1, Node l2)
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

        private Node MergeSortLinkedList(Node h, Node t = null)
        {
            // if input is empty or just a single node
            if (h == null || h.next == null) { return h; }
            // if (h == t) { return h; }

            // get middle node of linked list and its next node
            Node midNode = GetMiddleNode(h, t);
            Node midNodeNext = midNode.next;

            // severs the list into two parts
            midNode.next = null;

            Node firstHalf = MergeSortLinkedList(h, midNode);
            Node secondHalf = MergeSortLinkedList(midNodeNext, t);

            Node sortedList = MergeTwoLists(firstHalf, secondHalf);

            return sortedList;
        }

    }
}
