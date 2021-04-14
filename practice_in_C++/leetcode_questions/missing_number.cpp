#include <numeric>
#include <vector>
#include <iostream>


class Solution
{
public:
    int missingNumber(std::vector<int>& nums)
    {
        int n = nums.size();
        int sum = std::accumulate(nums.begin(), nums.end(), 0);
        int expectedSum = n * (n+1) / 2;
        return expectedSum - sum;
    }
};







#pragma region overly-complicated but still cool looking solution found on leetcode
// class Solution
// {
// public:
//     int missingNumber(vector<int> &nums)
//     {
//         std::sort(nums.begin(), nums.end());

//         int prev = 0;
//         int ret_qt = 0;
//         bool temp = true;
//         for (std::vector<int>::iterator it = nums.begin(); it < nums.end(); ++it)
//         {
//             std::cout << *(nums.end() - 1) << " , " << nums.size() << std::endl;
//             temp = *(nums.end() - 1) != nums.size();
//             std::cout << temp << std::endl;
//             if (*(nums.end() - 1) != nums.size())
//             {
//                 ret_qt = nums.size();
//                 break;
//             }
//             if (*it - prev > 1)
//             {
//                 std::cout << "found missing: " << *it - 1 << std::endl;
//                 ret_qt = *it - 1;
//                 break;
//             }
//             prev = *it;
//         }
//         return ret_qt;
//     }
// };
#pragma endregion