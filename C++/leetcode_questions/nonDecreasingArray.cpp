#include "../templates/template.h"

class Solution
{
private:
    bool cntInv(vector<int> nums)
    {
        int n = n = nums.size();
        for (int i = 1; i < n; ++i)
        {
            if (nums[i] < nums[i - 1])
            {
                return false;
            }
        }

        return true;
    }

public:
    bool checkPossibility(vector<int> &nums)
    {
        int invs = 0, n = nums.size(), left = 0, right = 0;

        for (int i = 1; i < n; ++i)
        {
            if (nums[i] < nums[i - 1])
            {
                left = i - 1;
                right = i;
                invs += 1;
            }

            if (invs > 1)
                return false;
        }

        if (invs == 0)
            return true;

        int tmp = nums[left];
        nums[left] = nums[right];

        bool ret = false;
        ret |= cntInv(nums);
        if (ret)
            return true;
        nums[left] = tmp;

        tmp = nums[right];
        nums[right] = nums[left];

        return ret || cntInv(nums);
    }
};

#pragma region online optimized solution
class OptimizedSolution
{
public:
    bool checkPossibility(vector<int> &nums)
    {
        int pos = -1, n = nums.size();

        for (int i = 0; i < n - 1; ++i)
        {
            if (nums[i] > nums[i + 1])
            {
                if (pos != -1)
                    return false;
                pos = i;
            }
        }

        return pos == -1 || pos == 0 || pos == n - 2 || nums[pos - 1] <= nums[pos + 1] || nums[pos] <= nums[pos + 2];
    }
};

#pragma endregion
