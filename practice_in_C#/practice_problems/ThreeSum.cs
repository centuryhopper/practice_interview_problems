using System;
using System.Collections.Generic;

public class ThreeSum
{
    public IList<IList<int>> threeSum(int[] ar)
    {
        int n = ar.Length;
        var l = new List<IList<int>>();
        if (n == 0 || n == 1) { return l; }

        Array.Sort(ar);

        for (int i = 0; i < n - 2; ++i)
        {
            // make sure we don't get a duplicate target of ar[i]
            if (i > 0 && ar[i] == ar[i - 1]) { continue; }

            int lo = i + 1, hi = n - 1;
            int targSum = 0 - ar[i];
            while (lo < hi)
            {
                int locSum = ar[lo] + ar[hi];
                if (locSum < targSum) { ++lo; }
                else if (locSum > targSum) { --hi; }
                else
                {
                    l.Add(new List<int>(3) { ar[i], ar[lo], ar[hi] });

                    // check for dupes so we don't have matching lists in our
                    // outer list
                    while (lo < hi && ar[lo] == ar[lo + 1]) { ++lo; }
                    while (lo < hi && ar[hi] == ar[hi - 1]) { --hi; }

                    // still need this operation to get
                    // to the next unique values
                    ++lo;
                    --hi;
                }
            }
        }

        return l;
    }
}