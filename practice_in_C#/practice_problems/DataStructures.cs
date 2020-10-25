using System;
using System.Collections.Generic;

namespace data_structures
{
    class DataStructures
    {
        /// <summary>
        // -array implementation with a predetermined size
        // -min heap by default
        // -we can only access the first element of the heap
        // -we can only insert after the last index of the heap
        /// </summary>
        /// <typeparam name="T"></typeparam>
        public class PriorityQueue<T> where T : IComparable<T>
        {
            private T[] ar;

            /// <summary>
            /// States the max number of elements the queue can hold
            /// </summary>
            private int arrayCapacity;

            /// <summary>
            /// number of elements in the heap.
            /// If the array isn't empty, this value should always be 1 greater
            /// than the index of the last element in the array
            /// </summary>
            public int size { get; private set; }
            public readonly bool isMaxHeap;

            /// <summary>
            /// default capacity of 16
            /// </summary>
            public PriorityQueue()
            {
                arrayCapacity = 16;
                size = 0;
                ar = new T[arrayCapacity];
            }

            // call the first constructor to create the list
            public PriorityQueue(IEnumerable<T> collection, bool isMaxHeap) : this()
            {
                this.isMaxHeap = isMaxHeap;

                foreach (var item in collection)
                {
                    Enqueue(item);
                }
            }

            // call the first constructor to create the list
            public PriorityQueue(bool isMaxHeap) : this()
            {
                this.isMaxHeap = isMaxHeap;
            }

            public PriorityQueue(int capacity, bool isMaxHeap)
            {
                ar = new T[capacity];
                this.arrayCapacity = capacity;
                this.size = 0;
                this.isMaxHeap = isMaxHeap;
            }

            // call the above constructor to default the bool to false
            public PriorityQueue(int capacity) : this(capacity, false) { }

            // default the bool to false by calling the constructor above
            public PriorityQueue(IEnumerable<T> collection) : this(collection, false) { }

            public T Peek()
            {
                if (IsEmpty())
                {
                    throw new InvalidOperationException("queue is empty");
                }

                return ar[0];
            }

            public bool IsEmpty() => arrayCapacity == 0;
            public bool isFull() => size == arrayCapacity;

            #region For percolating operations
                private int GetParentIndex(int child) => (child - 1) / 2;
                private int GetLeftChildIndex(int parent) => 2 * parent + 1;
                private int GetRightChildIndex(int parent) => 2 * parent + 2;

                /// <summary>
                // Return the index of whichever child of node 'parent' has the smallest
                // value. If the node at index 'parent' has no children, return parent.
                /// </summary>
                /// <param name="parent"></param>
                /// <returns></returns>
                private int GetIndexOfSmallerChild(int parent)
                {
                    int lc = GetLeftChildIndex(parent) >= this.size ? parent : GetLeftChildIndex(parent);
                    int rc = GetRightChildIndex(parent) >= this.size ? parent : GetRightChildIndex(parent);

                    T a = ar[lc], b = ar[rc];

                    return a.CompareTo(b) < 0 ? lc : rc;
                }

                private void swap(int i, int j)
                {
                    T tmp = ar[i]; ar[i] = ar[j]; ar[j] = tmp;
                }
            #endregion

            /// <summary>
            /// takes in the index of the element that was last inserted
            /// at the end of the heap
            /// </summary>
            /// <param name="childInd"></param>
            private void PercolateUp(int childInd)
            {
                int parentIndex = GetParentIndex(childInd);

                // minheap for now
                int switcheroo = isMaxHeap ? -1 : 1;
                while (switcheroo * ar[childInd].CompareTo(ar[parentIndex]) < 0)
                {
                    swap(childInd, parentIndex);

                    // adjust indices
                    childInd = parentIndex;
                    parentIndex = GetParentIndex(childInd);
                }
            }

            private void PercolateDown(int parentInd)
            {
                int childInd = GetIndexOfSmallerChild(parentInd);

                // // minheap only
                int switcheroo = isMaxHeap ? -1 : 1;
                while (switcheroo * ar[parentInd].CompareTo(ar[childInd]) > 0)
                {
                    swap(parentInd, childInd);

                    // adjust indices
                    parentInd = childInd;
                    childInd = GetIndexOfSmallerChild(parentInd);
                }
            }

            public void Enqueue(T item)
            {
                if (isFull()) { throw new InvalidOperationException("Queue is full"); }
                ar[size++] = item;

                // percolate up if necessary

                PercolateUp(size - 1);
            }

            /// <summary>
            /// return the first element
            /// </summary>
            /// <returns></returns>
            public T Dequeue()
            {
                T retVal = Peek();

                // dont percolate down if we just removed the last element in the heap
                if (--this.size == 0) { return retVal; }

                ar[0] = ar[size];

                // percolate down if necessary
                PercolateDown(0);

                return retVal;
            }

            public void PrintQueue()
            {
                for (int i = 0; i < size; ++i)
                {
                    print(ar[i]);
                }
            }

            private void print(T msg) => System.Console.WriteLine(msg);


        }
    }
}



