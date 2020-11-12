using System;
using System.Collections.Generic;

public class FourSum
{
    void p(object m) => Console.WriteLine(m);

    public IList<IList<int>> Four_Sum(int[] ar, int target)
    {
        int n = ar.Length;
        var l = new List<IList<int>>();

        if (n < 4) { return Array.Empty<IList<int>>(); }


        Array.Sort(ar);

        // Array.ForEach(ar, e => p(e));

        // we need four pointers to indexes for comparisons
        // i, j, lo, and hi

        for (int i = 0; i < n - 3; ++i)
        {
            // check for i dupes
            if (i > 0 && ar[i] == ar[i - 1]) { continue; }

            for (int j = i + 1; j < n; ++j)
            {
                // we might need to check for j dupes but probably not
                if ( j > i + 1 && ar[j] == ar[j - 1]) { continue; }

                int sum = target - (ar[i] + ar[j]);
                int lo = j + 1;
                int hi = n - 1;

                p(sum);

                while (lo < hi)
                {
                    int localSum = ar[lo] + ar[hi];
                    //p(localSum);
                    if (localSum < sum) { ++lo; }
                    else if (localSum > sum) { --hi; }
                    else
                    {
                        l.Add(new List<int>(4) { ar[i], ar[j], ar[lo], ar[hi] } );

                        // check dupes for lo and hi
                        while (lo < hi && ar[lo] == ar[lo + 1]) { ++lo; }
                        while (lo < hi && ar[hi] == ar[hi - 1]) { --hi; }

                        // still have to jump to the next index for a unique value
                        ++lo; --hi;
                    }
                }
            }
        }

        return l;




    }
}
