#include "../templates/template.h"


class Solution
{
private:
    int rec(string s1, int i, string s2, int j)
    {
        if (i == s1.length() || j == s2.length())
        {
            return 0;
        }

        int cnt = 0;

        if (s1[i] == s2[j])
        {
            cnt = 1 + rec(s1,i+1,s2,j+1);
        }
        else
        {
            int move1 = rec(s1,i+1,s2,j);
            int move2 = rec(s1,i,s2,j+1);
            int move3 = rec(s1,i+1,s2,j+1);
            // cout<<move1<<','<<move2<<','<<move3<<endl;
            cnt = max(max(move1,move2), move3);
            // cout<<cnt<<endl;
        }

        return cnt;
    }
    int rec_memo(string s1, int i, string s2, int j, vector<vi> memo)
    {
        if (i == s1.length() || j == s2.length())
        {
            return 0;
        }
        if (memo[i][j] != -1)
        {
            return memo[i][j];
        }

        int cnt = 0;

        if (s1[i] == s2[j])
        {
            cnt = 1 + rec(s1,i+1,s2,j+1);
        }
        else
        {
            int move1 = rec(s1,i+1,s2,j);
            int move2 = rec(s1,i,s2,j+1);
            // cout<<move1<<','<<move2<<endl;
            cnt = max(move1,move2);
            // cout<<cnt<<endl;
        }

        memo[i][j] = cnt;

        return cnt;
    }

public:
    int longestCommonSubsequence(string s1, string s2)
    {
//         vector<vi> memo(s1.length());
//         for (auto& v : memo)
//         {
//             v.resize(s2.length(),-1);
//             // p(v);
//             // nl
//         }

//         return rec_memo(s1,0,s2,0,memo);
        int m = s1.length(), n = s2.length();
        int dp[m+1][n+1];
        // memset(dp,0,sizeof(dp));
        // populate first row
        for (int j = 0; j <= n;++j)
        {
            dp[0][j] = 0;
        }
        // populate first column
        for (int i = 0;i <= m;++i)
        {
            dp[i][0] = 0;
        }

        for (int i = 1;i <= m; ++i)
        {
            for (int j = 1;j <= n;++j)
            {
                if (s1[i-1] == s2[j-1])
                {
                    dp[i][j] = dp[i-1][j-1] + 1;
                }
                else
                {
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }

        // for (int i =0;i<=m;++i)
        // {
        //     for (int j=0;j<=n;++j)
        //     {
        //         cout<<dp[i][j]<<' ';
        //     }
        //     nl
        // }

        return dp[m][n];
    }
};