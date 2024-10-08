#include<bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int search(vector<int>& nums, int target)
    {
        int l = 0, r = nums.size()-1;
        while (l <= r)
        {
            int mid = l + (r-l) / 2;
            int cur = nums[mid];
            if (cur == target) return mid;
            if (cur < target)
                l = mid + 1;
            else
                r = mid - 1;
        }

        return -1;
    }
};
