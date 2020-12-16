using System;
using System.Collections.Generic;

namespace practice_problems
{
    public class MergeTwoSortedArrays
    {
        void p(object m) => Console.WriteLine(m);

        public void Merge(int[] a, int m, int[] b, int n)
        {
            // cant merge if one of them is empty
            if (a.Length == 0 || b.Length == 0) { return; }

            List<int> lst = new List<int>(m + n);

            int i = 0, j = 0;

            /*

            [5,6,0,0,0], m = 2
            [1,4,5] n = 3
            ==> [1,4,5,5,6]


            Example:

            Input:
            nums1 = [1,2,3,0,0,0], m = 3
            nums2 = [2,5,6],       n = 3

            Output: [1,2,2,3,5,6]

            */

            while (i < m || j < n)
            {
                if (i < m)
                {
                    if (j < n)
                    {
                        if (a[i] < b[j])
                        {
                            // p("a");
                            // p("i = " + i);
                            lst.Add(a[i++]);
                        }
                        else if (a[i] == b[j])
                        {
                            // p("b");
                            //p("i = " + i);
                            lst.Add(a[i++]);
                            lst.Add(b[j++]);
                        }
                    }
                    else
                    {
                        lst.Add(a[i++]);
                    }

                }

                if (j < n)
                {
                    if (i < m)
                    {
                        if (b[j] < a[i])
                        {
                            lst.Add(b[j++]);
                        }
                        else if (b[j] == a[i])
                        {
                            // p("c");
                            // p("j = " + j);
                            lst.Add(a[i++]);
                            lst.Add(b[j++]);
                        }
                    }
                    else
                    {
                        //p("d");
                        //p("j = " + j);
                        lst.Add(b[j++]);
                    }
                }
            }

            int[] tmp = lst.ToArray();

            // merge
            tmp.CopyTo(a, 0);

        }
    }
}