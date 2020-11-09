using System;

namespace Game.Utils
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
        public static int[] SubArray(int[] data, int startingIndex, int endingIndex)
        {
            if (startingIndex >= endingIndex) { return Array.Empty<int>(); }

            // length of new array
            int length = endingIndex - startingIndex;
            int[] result = new int[length];
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


        static void print(object msg) => Console.WriteLine(msg);
    }
}

