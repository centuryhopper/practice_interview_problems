using System.Collections.Generic;
using data_structures;

namespace practice_problems
{
    public class TopKFrequentElements
    {
        public int[] TopKFrequent(int[] a, int k)
        {
            int n = a.Length;
            if (k > n || n < 2) { return a; }

            var d = new Dictionary<int, int>();

            // populate freq map
            for (int i = 0; i < n; ++i)
            {
                if (!d.ContainsKey(a[i]))
                {
                    d[a[i]] = 1;
                }
                else
                {
                    ++d[a[i]];
                }
            }

            // populate maxheap with freq map values
            var maxHeap =
            new PriorityQueue<KeyValuePair<int, int>>(d.Count, true, (pair1, pair2) => pair1.Value.CompareTo(pair2.Value));

            foreach (var pair in d)
            {
                maxHeap.Enqueue(pair);
            }

            maxHeap.PrintQueue();

            // create new array of size k and populate with maxheap values
            int[] retVal = new int[k];
            for (int i = 0; i < k; ++i)
            {
                retVal[i] = maxHeap.Dequeue().Key;
            }

            return retVal;
        }
    }

}