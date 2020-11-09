using System;
using System.Collections.Generic;

public class ArrayDegree
{
    public struct ElementInfo
    {
        public int freq;
        public int leftIndex;
        public int rightIndex;

        public ElementInfo(int f, int l, int r)
        {
            freq = f; leftIndex = l; rightIndex = r;
        }
    }

    public static int FindShortestSubArray(int[] a)
    {
        int n = a.Length;
        if (n <= 1) { return n; }

        var d = new Dictionary<int, ElementInfo>();

        int degree = 0, minLength = 1;

        for (int i = 0; i < n; ++i)
        {
            if (!d.ContainsKey(a[i]))
            {
                d[a[i]] = new ElementInfo(1, i, i);
            }
            else
            {
                // ++(d[a[i]].freq);
                d[a[i]] = new ElementInfo(d[a[i]].freq + 1, d[a[i]].leftIndex, i);
                // d[a[i]].rightIndex = i;

                if (d[a[i]].freq > degree)
                {
                    degree = d[a[i]].freq;

                    int diff = d[a[i]].rightIndex - d[a[i]].leftIndex + 1;
                    minLength = diff;
                }
                else if (d[a[i]].freq == degree)
                {
                    int diff = d[a[i]].rightIndex - d[a[i]].leftIndex + 1;
                    minLength = Math.Min(minLength, diff);
                }


            }
        }

        Console.WriteLine("degree: " + degree + " " + "minLength: " + minLength);


        return minLength;

    }
}