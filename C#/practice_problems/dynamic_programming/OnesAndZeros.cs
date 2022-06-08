using System;
using System.Linq;

public class OnesAndZeros
{
    #region
    /*
    Example 1:

    Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
    Output: 4
    Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
    Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
    {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
    Example 2:

    Input: strs = ["10","0","1"], m = 1, n = 1
    Output: 2
    Explanation: The largest subset is {"0", "1"}, so the answer is 2.
    */
    #endregion

    void p(object m) => Console.WriteLine(m);

    private int rec(string[] lst, int m, int n, int i)
    {
        if (i >= lst.Length)
        {
            return 0;
        }
        if (m + n == 0)
        {
            return 0;
        }
        int take = 0;
        int zeroes = lst[i].Count(c => c == '0');
        int ones = lst[i].Count(c => c == '1');

        if (m - zeroes >= 0 && n - ones >= 0)
        {
            take = 1 + rec(lst, m - zeroes, n - ones, i+1);
        }

        int dontTake = rec(lst, m, n, i+1);
        return Math.Max(take, dontTake);
    }

    private int rec_memo(string[] lst, int m, int n, int i, int[,,] memo)
    {
        if (m == 0 && n == 0)
        {
            return 0;
        }
        if (i >= lst.Length)
        {
            return 0;
        }
        if (memo[m,n,i] > 0)
        {
            return memo[m,n,i];
        }

        int take = 0;
        int zeroes = lst[i].Count(c => c == '0');
        int ones = lst[i].Count(c => c == '1');

        if (m - zeroes >= 0 && n - ones >= 0)
        {
            take = 1 + rec_memo(lst, m - zeroes, n - ones, i+1, memo);
        }

        int dontTake = rec_memo(lst, m, n, i+1, memo);

        memo[m,n,i] = Math.Max(take, dontTake);
        return memo[m,n,i];
    }

    public int FindMaxForm(string[] lst, int m, int n)
    {
        int[,,] memo = new int[m+1,n+1,lst.Length];

        int res = rec_memo(lst, m, n, 0, memo);

        return res;
    }
}