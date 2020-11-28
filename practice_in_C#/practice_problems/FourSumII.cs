using System.Collections.Generic;

public class FourSumII
{

    /*
        Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
    To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

    Example:
    Input:
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    Output:
    2
    Explanation:
    The two tuples are:
    1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
    2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0


    */

    public int FourSumCount(int[] A, int[] B, int[] C, int[] D)
        {
            int cnt = 0;

            // key will be the sum, value will be the number of occurrences
            var m = new Dictionary<int, int>();

            foreach (var c in C)
            {
                foreach (var d in D)
                {
                    int sum = c + d;
                    if (m.ContainsKey(sum))
                    {
                        ++m[sum];
                    }
                    else
                    {
                        m[sum] = 1;
                    }
                }
            }

            foreach (var a in A)
            {
                foreach (var b in B)
                {
                    int sum = a + b;
                    if (m.ContainsKey(-sum))
                    {
                        cnt += m[-sum];
                    }
                }
            }

            return cnt;
        }
}