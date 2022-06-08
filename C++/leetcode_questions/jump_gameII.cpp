#include "../templates/template.h"


class Solution
{

private:

    // brute force
    int rec(const vector<int>& nums, int i, int steps)
    {
        int localCnt = 1e9;
        if (i == nums.size() - 1)
        {
            return 0;
        }
        if (steps == 0)
        {
            // we can't go further, so return a
            // really big number to indicate that
            return 1e9;
        }

        for (int j = 1;j <= steps;++j)
        {
            if (i+j >= nums.size()) break;
            // if (nums[i+j] == 3)
            //     cout<<localCnt<<endl;

            // make choice of going j steps from current
            // position i and feed the number of steps in
            localCnt = min(localCnt, 1+rec(nums,i+j,nums[i+j]));
        }
        if (localCnt != 1e9)
            cout<<localCnt<<endl;

        return localCnt;
    }

    int rec_memo(const vector<int>& nums, int i, int steps, map<pii,int>& memo)
    {
        int localCnt = 1e9;
        if (i == nums.size() - 1)
        {
            return 0;
        }
        if (steps == 0)
        {
            // we can't go further, so return a
            // really big number to indicate that
            return 1e9;
        }

        if (memo.find({i, steps}) != memo.end())
            return memo[{i, steps}];

        for (int j = 1;j <= steps;++j)
        {
            if (i+j >= nums.size()) break;

            // if (nums[i+j] == 3)
            //     cout<<localCnt<<endl;

            // make choice of going j steps from current
            // position i and feed the number of steps in
            localCnt = min(localCnt, 1+rec_memo(nums,i+j,nums[i+j], memo));
        }
        // if (localCnt != 1e9)
        //     cout<<localCnt<<endl;
        memo[{i, steps}] = localCnt;

        return localCnt;
    }

public:

    int jump(vector<int>& nums)
    {
        if (nums.size() == 1 || nums[0] == 0) return 0;

        map<pii,int> m;
        int res = rec_memo(nums,0,nums[0], m);
        return res;
    }
};


/* DP Solution
class Solution:

    # tabular approach
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [float('inf')]*n
        dp[n-1] = 0

        # work backwards and populate dp array
        # based on the smallest value you can reach
        # and add 1 to its dp value at that index
        for i in range(n-2,-1,-1):
            # not reachable if current pos is 0
            if nums[i] == 0:
                continue
            reachableDist = (i+1)+nums[i]
            minVal = min(dp[i+1:reachableDist])
            # still cant reach
            if minVal == float('inf'):
                continue

            # find the smallest dp value from
            # the nums array and add 1
            dp[i] = minVal + 1

        # print(dp)


        return dp[0]
*/


/*
    // return the index of the rightmost max val
    int getRightMostMaxVal(const vector<int>& nums, int start, int end)
    {
        int val = start;
        int max = nums[start];
        for (int i = start;i <= end; ++i)
        {
            // >= for rightmost
            if (nums[i] >= max)
            {
                max = nums[i];
                val = i;
            }
        }

        return val;
    }

        int rec(const vector<int>& nums, int cur, int steps)
    {
        if (cur >= nums.size() - 1) return 0;
        if (steps == 0) return -1;

        int cnt = 0;
        int nextInd;
        if (cur+steps >= nums.size() - 1)
            nextInd = nums.size() - 1;
        else
            nextInd = getRightMostMaxVal(nums,cur+1,cur+steps);
        // cout<<nums[nextInd]<<endl;
        cnt = 1 + rec(nums,nextInd,nums[nextInd]);

        return cnt;
    }
*/