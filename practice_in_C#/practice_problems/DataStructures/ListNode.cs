
namespace data_structures
{
    /// <summary>
    /// represents a node in a singly linked list
    /// </summary>
    public class ListNode<T>
    {
        public T val;
        public ListNode<T> next;
        public ListNode(T val, ListNode<T> next = null)
        {
            this.val = val;
            this.next = next;
        }
    }
}
