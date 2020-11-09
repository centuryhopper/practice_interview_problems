using System;

namespace practice_problems
{
    public class ArrayPartitionI
    {
        public int ArrayPairSum(int[] a)
        {
            Array.Sort(a);

            int n = a.Length;
            int s = 0;

            for (int i = 0; i < n - 1; i += 2)
            {
                s += Math.Min(a[i], a[i + 1]);
            }

            return s;
        }
    }
}