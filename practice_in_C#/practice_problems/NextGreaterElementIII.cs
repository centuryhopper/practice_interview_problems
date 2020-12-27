using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
//  reversing an int:
//         int tmp = 321;
//         while (tmp > 0)
//         {
//             retVal += (tmp % 10);
//             retVal *= 10;
//             tmp /= 10;
//         }
//         retVal /= 10;
//         p(retVal);
    static void p (object m) => Console.WriteLine(m);


    public int NextGreaterElement(int n)
    {
        string s = n.ToString();
        var lst = s.Select(c => Convert.ToInt32(c - '0')).ToList<int>();

        // lst.ForEach(e => p(e));

        int smallerNumberIndex = lst.Count - 2;
        while (smallerNumberIndex >= 0 && lst[smallerNumberIndex] >= lst[smallerNumberIndex + 1])
        {
            smallerNumberIndex--;
        }

        if (smallerNumberIndex == -1) return -1;

        int biggerNumberIndex = lst.Count - 1;
        while (lst[biggerNumberIndex] <= lst[smallerNumberIndex])
        {
            biggerNumberIndex--;
        }

        void swap(List<int> l, int x, int y)
        {
            int tmp = l[x];
            l[x] = l[y];
            l[y] = tmp;
        }

        swap(lst, smallerNumberIndex, biggerNumberIndex);

        lst.Reverse(smallerNumberIndex + 1, lst.Count - (smallerNumberIndex + 1));

        dynamic res = "";

        foreach (int elem in lst)
        {
            res += elem;
        }

        res = Convert.ToUInt64(res);

        return res >= int.MaxValue ? -1: (int) res;
    }

}