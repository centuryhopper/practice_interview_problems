using System.Collections.Generic;


/// <summary>
/// At EACH step we have two choices: either take one step or take two steps
/// </summary>
public class ClimbingStairs
{
    // brute force
    private int helper_recursive(int n)
    {
        if (n < 2)
        {
            return 1;
        }

        return helper_recursive(n - 1) + helper_recursive(n - 2);
    }

    // memoization
    private int helper_memo(int n, Dictionary<int, int> memo)
    {
        // if it's in our hashmap already then just return it
        if (memo.ContainsKey(n))
        {
            return memo[n];
        }

        // usual base case
        if (n < 2)
        {
            memo[n] = 1;
            return 1;
        }

        // cache result and return it at each step (recursive call)
        memo[n] = helper_memo(n - 1, memo) + helper_memo(n - 2, memo);

        return memo[n];
    }

    // dynamic programming approach
    private int helper_dp(int n)
    {
        int[] dp = new int[n + 1];

        dp[0] = dp[1] = 1;

        for (int i = 2; i <= n; ++i)
        {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[n];
    }

    // optimized dynamic programming approach
    private int helper_dp_optimized(int n)
    {
        int[] dp = new int[2];

        dp[0] = dp[1] = 1;

        for (int i = 2; i <= n; ++i)
        {
            dp[i % 2] = dp[(i - 1) % 2] + dp[(i - 2) % 2];
        }

        return dp[n % 2];
    }

    public int ClimbStairs(int n)
    {
        return helper_memo(n, new Dictionary<int, int>());
    }
}