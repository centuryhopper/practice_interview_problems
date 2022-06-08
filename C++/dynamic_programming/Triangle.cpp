#include "templates/template.h"

class Solution
{

private:
    int rec(vector<vector<int>>& triangle, int i, int j)
    {
        if (i>=triangle.size() || j>=triangle[i].size())
        {
            return 0;
        }

        int sameIndex = rec(triangle,i+1,j);
        int nextIndex = rec(triangle,i+1,j+1);

        return triangle[i][j] + min(sameIndex,nextIndex);
    }

    int dp_way(const vvi& tri, vvi& dp)
    {
        int minVal = INT_MAX;
        dp.resize(tri.size());
        dp[0] = tri[0];
        // for (auto val:dp)
        //     p(val)
        for (int i=1;i<tri.size();++i)
        {
            int rowSize = tri[i].size();
            dp[i].resize(rowSize);
            // for (auto val:dp)
            // {
            //     p(val)
            //     cout<<endl;
            // }
            for (int j=0;j<rowSize;++j)
            {
                if (j == 0)
                {
                    int sameIndex = tri[i][j] + dp[i-1][j];
                    dp[i][j] = sameIndex;
                }

                else if (j == rowSize-1)
                {
                    int prevIndex = tri[i][j] + dp[i-1][j-1];
                    dp[i][j] = prevIndex;
                }
                else
                {
                    int sameIndex = tri[i][j] + dp[i-1][j];
                    int prevIndex = tri[i][j] + dp[i-1][j-1];
                    dp[i][j] = min(sameIndex, prevIndex);
                }

                // at the last row
                // if (i == tri.size()-1)
                //     minVal = min(minVal, dp[i][j]);
            }
            // for (auto val:dp)
            // {
            //     p(val)
            //     cout<<endl;
            // }
            // cout<<endl;
        }
        int lastRow=dp.size()-1;
        int lastRowSize = dp[lastRow].size();
        for (int i = 0; i < lastRowSize;++i)
            minVal = min(minVal, dp[lastRow][i]);

        return minVal;
    }

public:
    int minimumTotal(vector<vector<int>>& triangle)
    {
        // return rec(triangle,0,0);
        vvi dp;
        return dp_way(triangle, dp);
    }
};