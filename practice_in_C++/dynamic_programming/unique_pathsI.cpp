#include "../templates/template.h"

class Solution
{

private:
    // int memo[100][100];
    // memset(memo,-1,sizeof(memo));

    // brute force recursion
    int rec(int i, int j, int m, int n)
    {
        if (i>=m || j>=n) return 0;
        if (i==m-1 && j==n-1) return 1;

        // go right and go down
        return rec(i+1,j,m,n) + rec(i,j+1,m,n);
    }

//     int recMemo(int i, int j, int m, int n)
//     {
//         if (i>=m || j>=n) return 0;
//         if (i==m-1 && j==n-1) return 1;
//         if (memo[i][j] != -1) return memo[i][j];

//         // go right and go down
//         return memo[i][j] = rec(i+1,j,m,n) + rec(i,j+1,m,n);
//     }

    long long dpWay(int m, int n)
    {
        long long dp[m][n];
        // there is only one way to get to each location in the first row and column
        int i,j;
        // first row
        for (i = 0;i < n; ++i) dp[0][i] = 1;
        // first column
        for (i = 0;i < m; ++i) dp[i][0] = 1;

        for (i = 1;i < m; ++i)
        {
            for (j = 1;j < n; ++j)
            {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }

        return dp[m-1][n-1];
    }

public:
    long long uniquePaths(int m, int n)
    {
        // return recMemo(0,0,m,n);
        return dpWay(m,n);
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    cout << s.uniquePaths(100,100) << endl;

    return 0;
}