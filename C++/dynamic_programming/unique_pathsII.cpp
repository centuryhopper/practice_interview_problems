#include "../templates/template.h"

class Solution
{
private:
    int ways = 0;
    int dp[100][100];
    void rec(vvi grid, int i, int j)
    {
        // check bounds
        if (i >= grid.size() || j >= grid[0].size())
            return;
        // check obstacle
        if (grid[i][j] == 1)
            return;
        // check if reached goal
        if (i == grid.size() - 1 && j == grid[0].size() - 1)
        {
            ++ways;
            return;
        }

        // recurse down
        rec(grid, i+1, j);
        // recurse right
        rec(grid, i, j+1);
    }

    void dp_way(const vvi& grid)
    {
        int m = grid.size(), n = grid[0].size();
        memset(dp, 0, sizeof(dp));
        dp[0][0] = 1;

        // first row
        for (int i = 1; i < n; ++i)
        {
            // not obstacle
            if (grid[0][i] == 0)
            {
                dp[0][i] = dp[0][i-1];
            }
            // obstacle
            else
            {
                dp[0][i] = 0;
            }
        }

        // first column
        for (int i = 1; i < m; ++i)
        {
            // not obstacle
            if (grid[i][0] == 0)
            {
                dp[i][0] = dp[i-1][0];
            }
            // obstacle
            else
            {
                dp[i][0] = 0;
            }
        }

        // all other rows
        for (int i = 1; i < m; ++i)
        {
            for (int j = 1; j < n; ++j)
            {
                // not obstacle
                if (grid[i][j]==0)
                {
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                }
                else
                {
                    dp[i][j] = 0;
                }
            }
        }

        // for (int i=0;i<m;++i)
        // {
        //     for (int j=0;j<n;++j)
        //         cout<<dp[i][j]<<' ';
        //     cout<<endl;
        // }


    }

public:
    int uniquePathsWithObstacles(vector<vector<int>>& grid)
    {
        // rec(grid,0,0);
        // return ways;
        // can't solve the grid if the start location is blocked
        if (grid[0][0] == 1) return 0;
        int m = grid.size(), n = grid[0].size();
        // cout<<m<<' '<<n<<endl;
        dp_way(grid);

        return dp[m-1][n-1];
    }
};