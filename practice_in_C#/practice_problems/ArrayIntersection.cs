using System;
using System.Collections.Generic;

public class ArrayIntersection
{
    // brute force:
    // sort array, then compare


    // my thought process:
    // find smaller lengthed array,
    // and loop that many times to compare

    // assumes the length of ar1 is smaller than or equal to the length of ar2
    private int[] CompareAndAdd(int[] ar1, int[] ar2)
    {
        int n = ar1.Length, n2 = ar2.Length;
        var lst = new List<int>();

        // loop smaller length times
        // inner loop will iterate longer length times
        // this technique will also work if the lengths
        // are the same
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n2; ++j)
            {
                if (ar1[i] == ar2[j])
                {
                    lst.Add(ar1[i]);
                    // Console.WriteLine(ar1[i]);

                    // mark it as dirty
                    if (ar2[j] == int.MinValue)
                    {
                        ar2[j] = int.MaxValue - 1;
                    }
                    else if (ar2[j] == 0)
                    {
                        ar2[j] = int.MaxValue - 1;
                    }
                    else
                    {
                        ar2[j] *= -1;
                    }


                    break;
                }
            }
        }

        return lst.ToArray();
    }


    public int[] Intersect(int[] nums1, int[] nums2)
    {
            if (nums1.Length == 0) { return nums1; }
            if (nums2.Length == 0) { return nums2; }

            bool nums1IsGreater = nums1.Length > nums2.Length;

            // new array will hold as many values or less than
            // as the smaller lengthed array
            int[] ret;

           if (nums1IsGreater)
           {
               // pass the smaller one in first
              ret = CompareAndAdd(nums2, nums1);
           }
           else
           {
              ret = CompareAndAdd(nums1, nums2);
           }

        // Console.WriteLine(ret[i]);

        return ret;


       // return nums1.Intersect(nums2).ToArray();
    }
}