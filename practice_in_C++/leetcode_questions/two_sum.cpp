#include <cstdint>
#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <climits>
#include <iterator>
#include <vector>
#include <map>

#define print(x) std::cout << x << std::endl;
#define fl(i, k, n) for (int i = k; i < n; ++i)
using namespace std;

// Given an array of integers nums and an integer target, return indices
// of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may
// not use the same element twice.

// You can return the answer in any order.

// example nums = [2, 7, 11, 15], target = 9  => 2 + 7 = 9 =>  indices: [0,1]

// the array may or may not be sorted

class TwoSum
{
    public:
        TwoSum()
        {
            print("no parameters");
        }

        TwoSum(int hi)
        {
            print("hello " + to_string(hi));
        }

        ~TwoSum()
        {
            print("destroying object");
        }

        vector<int> twoSum(vector<int> &nums, int target)
        {
            std::map<int, int> m;
            int i, n = nums.size();
            vector<int> retVal;
            fl(i, 0, n)
            {
                if (m.count(target - nums[i]))
                {
                    retVal.emplace_back(i);
                    retVal.emplace_back(m[target - nums[i]]);
                    return retVal;
                }

                m[nums[i]] = i;
            }

            return retVal;
        }
};

int main(int argc, char const *argv[])
{
    vector<int> nums {15, 11, 7, 2};

    TwoSum ts;
    int target = 17;
    vector<int> res = ts.twoSum(nums, target);

    int i;
    print("indices of the numbers that add up to the target value: " + to_string(target));
    fl(i, 0, res.size())
    {
        print(res[i]);
    }


    return 0;
}
