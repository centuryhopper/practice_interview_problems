#include<vector>
#include<iostream>
#include<cmath>
#include<algorithm>


#define p(x) std::cout << x << "\n";
using namespace std;

class Solution
{
private:
    int rec(vector<int> lst, int prevVal, int curInd)
    {
        if (curInd >= lst.size()) return 0;
        cout << prevVal << ',' << lst[curInd] << "\n";

        // either take the current value and add 1 to count or don't take it
        // and move on to next value
        int take = 0;
        if (lst[curInd] > prevVal)
        {
            take = 1 + rec(lst, lst[curInd], curInd + 1);
        }
        int dontTake = rec(lst, prevVal, curInd + 1);

        return max(take, dontTake);
    }

    int recMemo(vector<int> lst, int prevInd, int curInd, int** memo)
    {
        if (curInd >= lst.size()) return 0;
        // cout << prevInd << ',' << curInd << "\n";
        if (memo[prevInd+1][curInd] != -1)
        {
            return memo[prevInd+1][curInd];
        }

        // either take the current value and add 1 to count or don't take it
        // and move on to next value
        int take = 0;
        if (prevInd < 0 || lst[curInd] > lst[prevInd])
        {
            // prevInd will be our current recursive call's current index in the next recursive call
            take = 1 + recMemo(lst, curInd, curInd + 1, memo);
        }
        int dontTake = recMemo(lst, prevInd, curInd + 1, memo);

        memo[prevInd+1][curInd] = max(take, dontTake);

        return memo[prevInd+1][curInd];
    }

public:
    int lengthOfLIS(vector<int>& lst)
    {
        int n = lst.size();
        int dp[n];
        for (int i = 0;i < n;++i)
            dp[i] = 1;
        // memset(dp, -1, sizeof(dp));
        int retMax = 1;
        for (int cur = 1; cur < n; ++cur)
        {
            for (int aux = 0; aux < cur; ++aux)
            {
                if (lst[aux] < lst[cur])
                {
                    dp[cur] = max(dp[cur], dp[aux] + 1);
                    retMax = max(retMax, dp[cur]);
                }
            }
        }

        // for (int i = 0;i < n;++i)
        //     printf("%d ", dp[i]);
        // printf("\n");


        return retMax;



        // n + 1 because our prev index will start at -1
        // to make sure that we try both paths at the value
        // at the first index (i.e. recurse on the possibilities that we count the first element or don't count it)
        // int memo[n+1][n];
        // memset(memo, -1, sizeof(memo));
//         int** memo = new int*[n+1];
//         for (int i = 0; i < n+1;++i)
//         {
//             memo[i] = new int[n];
//             for (int j = 0;j < n;++j)
//             {
//                 memo[i][j] = -1;
//                 // printf("%d ", memo[i][j]);
//             }
//             // printf("\n");
//         }
//         int res = recMemo(nums,-1,0, memo);

//         for(int i = 0;i < n+1;++i)
//             delete[] memo[i];
//         delete[] memo;
//         // start prev val at int_min because we want to trigger both recursive calls
//         // upon starting out in this function
//         return res;
    }
};

#pragma region more optimized solution
/*
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n,0);
        int length=1;
        dp[0]=nums[0];
        for(int i=1;i<n;i++){
            auto pos = lower_bound(dp.begin(),dp.begin()+length,nums[i]);
            if(pos==dp.begin()+length){
                dp[length] = nums[i];
                length++;
            }
            else{
                *pos=nums[i];
            }
        }

        return length;
    }
};

*/
#pragma endregion