using System;
using data_structures;

namespace practice_problems
{
    public class FindKthSmallestElementIn2DMatrix
    {
        void p(object m) => Console.WriteLine(m);

        public int KthSmallest(int[][] a, int k)
        {
            int numRow = a.Length, numColumn = a[0].Length;

            PriorityQueue<int> maxheap = new PriorityQueue<int>(k + 1, true, (int a, int b) => a.CompareTo(b));

            for (int i = 0; i < numRow; ++i)
            {
                for (int j = 0; j < numColumn; ++j)
                {
                    maxheap.Enqueue(a[i][j]);

                    // makes sure the kth smallest is always reachable when returning a value
                    if (maxheap.size > k) { maxheap.Dequeue(); }
                }
            }

            return maxheap.Peek();
        }
    }
}