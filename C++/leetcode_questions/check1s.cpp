
#include <vector>
using namespace std;

class Solution
{
public:
    bool kLengthApart(vector<int> &nums, int k)
    {
        vector<int> v;
        v.reserve(nums.size());

        for (int i = 0; i < nums.size(); ++i)
        {
            if (nums[i] == 1)
            {
                v.emplace_back(i);
            }
        }

        if (v.size() > 1)
        {
            for (int j = 1; j < v.size(); ++j)
            {
                if ((v[j] - v[j - 1]) - 1 < k)
                {
                    return false;
                }
            }
        }

        return true;
    }
};