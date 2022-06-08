class Solution
{
public:
    vector<int> findErrorNums(vector<int> &nums)
    {
        // std::sort(nums.begin(), nums.end());

        vector<int> ret;
        map<int, int> m;

        // find duplicate
        for (int i = 0; i < nums.size(); ++i)
        {
            if (m.count(nums[i]))
            {
                ret.emplace_back(nums[i]);
            }
            else
            {
                m[nums[i]] = 1;
            }
        }

        // find missing number
        for (int i = 1; i < nums.size() + 1; ++i)
        {
            if (!m.count(i))
            {
                ret.emplace_back(i);
                break;
            }
        }

        return ret;
    }
};