using System;

namespace practice_problems
{
    public class ValidMountainArray
    {
        bool isAMountain = true;

        void traverser(int[] ar, int i, int j, int peakInd)
        {
            // if the array pointers cross each other, we're done
            if (i >= j) { return; }

            if (i < peakInd)
            {
                //Console.WriteLine("i: " + i);
                isAMountain &= ar[i] < ar[i + 1];
            }


            if (j > peakInd)
            {
                //Console.WriteLine("j: " + j);
                isAMountain &= ar[j] < ar[j - 1];
            }

            // stop searching early if this bool flips
            if (!isAMountain) { Console.WriteLine(isAMountain); return; }

            // avoid any array pointers from being at the index
            // of our max value.
            traverser(ar, i < peakInd ? i + 1 : i, j > peakInd ? j - 1 : j, peakInd);
        }

        // returns the max value along with its index
        (int, int) findMaxAndIndex(int[] ar, int len)
        {
            int max = ar[0];
            int ind = 0;

            for (int i = 1; i < len; ++i)
            {
                if (ar[i] > max)
                {
                    max = ar[i]; ind = i;
                }
            }

            return (max, ind);
        }

        public bool validMountainArray(int[] ar)
        {
            int n = ar.Length;
            if (n < 3) { return false; }

            (int max, int ind) = findMaxAndIndex(ar, n);

            if (max == ar[n - 1] || max == ar[0]) { return false; }

            // Console.WriteLine(max + " " + ind);

            traverser(ar, 0, n - 1, ind);

            return isAMountain;
        }
    }
}