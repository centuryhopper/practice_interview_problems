using System;

namespace Utils
{
    public static class Utils
    {
        /// <summary>
        /// given an int array, return a subarray of values
        /// starting from the given array's "startingIndex" to,
        /// but not including, the "endingIndex"
        /// </summary>
        /// <param name="data"></param>
        /// <param name="startingIndex"></param>
        /// <param name="endingIndex"></param>
        /// <returns></returns>
        public static T[] SubArray<T>(this T[] data, int startingIndex, int? endingIndex = null)
        {
            if (endingIndex == null) { endingIndex = data.Length; }
            if (startingIndex < 0 || endingIndex <= 0) { return Array.Empty<T>(); }
            if (startingIndex >= endingIndex) { return Array.Empty<T>(); }

            // length of new array
            int length = endingIndex.GetValueOrDefault() - startingIndex;
            T[] result = new T[length];
            Array.Copy(data, startingIndex, result, 0, length);
            return result;
        }

        /// <summary>
        /// given an integer array,
        /// this method will return a
        /// tuple containing the max value
        /// and the index of which it is found,
        /// respectively
        /// </summary>
        /// <param name="a"></param>
        /// <returns></returns>
        public static (int, int) findMax(int[] a)
        {
            int max = int.MinValue;
            int idx = 0;

            for (int i = 0; i < a.Length; ++i)
            {
                int tmp = max;
                max = Math.Max(max, a[i]);
                if (max > tmp) { idx = i; }
            }

            // returns the max value and the index of it all in one iteration
            return (max, idx);
        }

        public class ArrayShuffleAndReset
        {
            private int[] a, b;
            private Random r;

            private void swap(int[] ar, int i, int j)
            {
                if (i == j) { return; }

                int tmp = ar[i]; ar[i] = ar[j]; ar[j] = tmp;
            }

            public ArrayShuffleAndReset(int[] nums)
            {
                a = new int[nums.Length];
                r = new Random();

                // this makes a point to its own array rather than keep a
                // reference to nums,
                // which would look like a = nums;
                nums.CopyTo(a, 0);
                b = nums;
            }

            /** Resets the array to its original configuration and return it. */
            public int[] Reset()
            {
                return b;
            }

            /** Returns a random shuffling of the array. */


            // fisher-yates algorithm
            public int[] Shuffle()
            {
                for (int i = a.Length - 1; i >= 0; --i)
                {
                    int next = r.Next(i + 1);
                    swap(a, i, next);
                }

                return a;
            }
        }


        static void print(object msg) => Console.WriteLine(msg);
    }
}

