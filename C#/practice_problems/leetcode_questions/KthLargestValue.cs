
using System;
using System.Collections.Generic;

namespace practice_problems
{
    public class KthLargestValue
    {
        public static int FindKthLargest(int[] nums, int k)
        {
            var minheap = new SortedList<int, int>();
            int size = 0;

            foreach (var num in nums)
            {
                minheap[num] = minheap.ContainsKey(num) ? minheap[num] + 1 : 1;
                size++;
                if (size > k)
                {
                    if (--minheap[minheap.Keys[0]] <= 0)
                    {
                        minheap.RemoveAt(0);
                    }
                    size--;
                }
            }

            // foreach (var kvp in minheap)
            // {
            //     Console.WriteLine($"{kvp.Key} : {kvp.Value}");
            // }

            return minheap.Keys[0];
        }
    }
}

    //     // simulate a priority queue
    //     var d = new SortedDictionary<int, int>();

    //     int values = 0;

    //     foreach (var num in nums)
    //     {
    //         d[num] = d.ContainsKey(num) ? d[num] + 1 : 1;
    //         ++values;

    //         if (values > k)
    //         {
    //             // pop the smallest one
    //             var kvp = d.First();
    //             if (kvp.Value > 1)
    //             {
    //                 d[kvp.Key]--;
    //             }
    //             else
    //             {
    //                 d.Remove(kvp.Key);
    //             }

    //             --values;
    //         }
    //     }

    //    // System.Console.WriteLine(string.Join(",", d.ToArray()));

    //     return d.First().Key;