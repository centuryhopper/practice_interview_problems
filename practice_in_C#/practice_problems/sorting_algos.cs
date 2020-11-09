using System;


namespace sorting_algos
{
    public static class SortingAlgos
    {
        public static void PrintArray(int[] array)
        {
            if (array.Length == 0)
            {
                System.Console.WriteLine("array is empty");
                return;
            }

            Array.ForEach(array, elem => System.Console.WriteLine(elem));
        }

        private static void Swap(int[] ar, int a, int b)
        {
            int tmp = ar[a]; ar[a] = ar[b]; ar[b] = tmp;
        }

        #region MERGE SORT
        public static void MergeSort(int[] array)
        {
            MergeSort(array, 0, array.Length - 1);
        }

        private static void MergeSort(int[] array, int lo, int hi)
        {
            // base case
            if (lo >= hi)
            {
                return;
            }

            // get mid value
            int mid = lo + ((hi - lo) / 2);

            // left half
            MergeSort(array, lo, mid);

            // right half
            MergeSort(array, mid + 1, hi);

            // Mergey-Merge
            MergeyMerge(array, lo, mid, hi);

        }

        /// <summary>
        /// start copying values into the new array
        /// </summary>
        /// <param name="array">The array to be merged</param>
        /// <param name="lo">lower bound index</param>
        /// <param name="mid">mid index</param>
        /// <param name="hi">upper bound index</param>
        private static void MergeyMerge(int[] array, int lo, int mid, int hi)
        {
            // hi - lo + 1 because arrays have zero-based indexing
            int[] aux = new int[hi - lo + 1];

            // cached values for readability purposes
            int leftHalfStart = lo;
            int leftHalfEnd = mid;
            int rightHalfStart = mid + 1;
            int rightHalfEnd = hi;

            int copyingIndex = 0;

            while (leftHalfStart <= leftHalfEnd || rightHalfStart <= rightHalfEnd)
            {
                // check bounds

                // if left half start index goes out of bounds,
                // copy rest of right half values into aux array
                // or vice versa
                if (leftHalfStart > leftHalfEnd)
                {
                    aux[copyingIndex++] = array[rightHalfStart++];
                }
                else if(rightHalfStart > rightHalfEnd)
                {
                    aux[copyingIndex++] = array[leftHalfStart++];
                }
                // otherwise, we compare values and copy accordingly
                else if (array[leftHalfStart] < array[rightHalfStart])
                {
                    aux[copyingIndex++] = array[leftHalfStart++];
                }
                else
                {
                    aux[copyingIndex++] = array[rightHalfStart++];
                }
            }

            // copy merged portion back into original array
            for (int i = lo; i <= hi; ++i)
            {
                array[i] = aux[i - lo];
            }
        }
        #endregion

        #region BUBBLE SORT

        public static void OptimizedBubbleSort(int[] ar)
        {
            bool didSwap = false;
            int n = ar.Length;

            // stop before the last element because if
            // we stopped at the last element, our
            // algorithm will check the non-existing
            // next element after and we'll get
            // an array index outta bounds exception
            for (int i = 0; i < n - 1; ++i)
            {
                // bubble sort needs to swap on every iteration
                didSwap = false;

                // (ar.Length - 1) - i because we need to shrink our
                // upper bound for every number we pass
                for (int j = 0; j < (n - 1) - i; ++j)
                {
                    if (ar[j] > ar[j+1])
                    {
                        Swap(ar, j, j+1);
                        didSwap = true;
                    }
                }

                // leave the algorithm early if no swapping at all occurred
                if (!didSwap) { break; }
            }
        }

        #endregion

    }
}





