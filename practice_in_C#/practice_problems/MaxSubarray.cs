using System;

namespace practice_problems
{
    public class MaxSubarray
    {

        // Kadane's algorithm dp
        public int MaxSubArray(int[] a)
        {
            if (a.Length == 1) { return a[0]; }

            int n = a.Length;

            long s = int.MinValue, max = int.MinValue;
            for (int i = 0; i < n; ++i)
            {
                s = Math.Max(a[i], s + a[i]);
                max = Math.Max(max, s);
            }

            //if (max >= int.MaxValue)
            // {
            //     max = int.MaxValue - 1;
            // }
            // else if (max < int.MinValue)
            // {
            //     max = int.MinValue;
            // }


            return (int)max;
        }
    }
}
