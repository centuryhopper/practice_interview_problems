// Sean Szumlanski
// COP 3503, Summer 2019

// Binomial.java
// =============
// Dynamic programming solution to the binomial coefficients problem. (Includes
// standard recursive implementation and memoization versions, as well.)


// Converted to C# language by Leo Zhang on 12/27/2020
using System;
using System.Collections.Generic;

namespace DP
{
    public class Binomial
    {
        private const int UNINITIALIZED = -1;

        // Standard recursive implementation.
        public static int choose(int n, int k)
        {
            if (k == 0 || k == n)
                return 1;

            return choose(n - 1, k - 1) + choose(n - 1, k);
        }

        // Memoization version (with 2D array).
        public static int chooseMemo(int n, int k)
        {
            int[][] memo = new int[n + 1][];

            for (int i = 0; i < n + 1; ++i)
            {
                memo[i] = new int[k + 1];
            }

            // System.Console.WriteLine(memo.Length);

            for (int i = 0; i <= n; i++)
                Array.Fill<int>(memo[i], UNINITIALIZED);

            return chooseMemo(n, k, memo);
        }

        private static int chooseMemo(int n, int k, int[][] memo)
        {
            if (k == 0 || k == n)
            {
                memo[n][k] = 1;
                return 1;
            }

            if (memo[n][k] != UNINITIALIZED)
                return memo[n][k];

            memo[n][k] = chooseMemo(n - 1, k - 1, memo) + chooseMemo(n - 1, k, memo);
            return memo[n][k];
        }

        // Memoization version (with HashMap).
        public static int chooseUltraMemo(int n, int k)
        {
            var memo = new Dictionary<(int, int), int>();
            return chooseUltraMemo(n, k, memo);
        }

        private static int chooseUltraMemo(int n, int k, Dictionary<(int, int), int> memo)
        {
            if (k == 0 || k == n)
                return 1;

            // int? memoized = memo[(n, k)];
            // if (memoized != null)
            //     return memoized.GetValueOrDefault();

            if (memo.ContainsKey((n, k)))
            {
                return memo[(n,k)];
            }

            int result = chooseUltraMemo(n - 1, k - 1, memo) + chooseUltraMemo(n - 1, k, memo);
            memo[(n, k)] = result;
            return result;
        }

        // Dynamic programming version.
        public static int chooseDP(int n, int k)
        {
            int[][] binom = new int[n + 1][];

            for (int i = 0; i < n + 1; ++i)
            {
                binom[i] = new int[k + 1];
            }

            // Recall that choose(n, 0) = 1.
            for (int i = 0; i <= n; i++)
                binom[i][0] = 1;

            // Recall that choose(n, n) = 1.
            for (int i = 0; i <= k; i++)
                binom[i][i] = 1;

            // Note that I haven't worried about initializing binom[i][j] to zero in cases
            // where j > i. (Recall that choose(n, k) = 0 if k > n.) There are two reasons
            // for this: (1) Java will initialize those to zero for us, and (2) the code
            // below carefully avoids referencing cells where to column exceeds the row.

            // Here, we restrict col to ensure we don't go out of bounds (while also
            // avoiding some unnecessary computation in cases where col > row). Also,
            // notice that we will have filled in all the non-zero cells in the first
            // two rows in our base case initialization, so we can skip directly to
            // the third row (row = 2).
            for (int row = 2; row <= n; row++)
                for (int col = 1; col <= Math.Min(row - 1, k); col++)
                    binom[row][col] = binom[row - 1][col - 1] + binom[row - 1][col];

            return binom[n][k];
        }
    }

}

