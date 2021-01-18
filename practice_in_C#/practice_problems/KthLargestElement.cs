
using System.Linq;
using System.Collections.Generic;


public class KthLargestElement
{
    public int FindKthLargest(int[] nums, int k)
    {
        // simulate a priority queue
        var d = new SortedDictionary<int, int>();

        int values = 0;

        foreach (var num in nums)
        {
            d[num] = d.ContainsKey(num) ? d[num] + 1 : 1;
            ++values;

            if (values > k)
            {
                // pop the smallest one
                var kvp = d.First();
                if (kvp.Value > 1)
                {
                    d[kvp.Key]--;
                }
                else
                {
                    d.Remove(kvp.Key);
                }

                --values;
            }
        }

        // System.Console.WriteLine(string.Join(",", d.ToArray()));

        return d.First().Key;
    }

}