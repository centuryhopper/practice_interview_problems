#include "../templates/template.h"

class Solution
{
private:
    vector<int> lst;

    void bin_search(vector<int> nums, int target, int lo, int hi)
    {
        if (lo > hi)
        {
            vector<int> v{-1, -1};
            lst.reserve(2);
            lst.insert(lst.end(), v.begin(), v.end());
            return;
        }

        // prevent int overflow using this mid formula
        int mid = lo + (hi - lo) / 2;

        if (nums[mid] > target)
        {
            bin_search(nums, target, lo, mid - 1);
        }
        else if (nums[mid] < target)
        {
            bin_search(nums, target, mid + 1, hi);
        }
        else
        {
            int lb = mid, ub = mid;
            // cout<<nums[ub+1]<<endl;

            // find boundaries;
            while (true)
            {
                if (lb - 1 >= 0 && nums[lb - 1] == target)
                    --lb;
                else if (ub + 1 < nums.size() && nums[ub + 1] == target)
                    ++ub;
                else
                    break;
            }

            lst.push_back(lb);
            lst.push_back(ub);
        }
    }

public:
    vector<int> searchRange(vector<int> &nums, int target)
    {
        bin_search(nums, target, 0, nums.size() - 1);
        return lst;
    }
};

#pragma region optimized online solution

// class Solution {
// public:

//     int findLowerEnd(vector<int>& nums,int& target){
//         int numsLength = nums.size();
//         int start = 0 , end = numsLength - 1;
//         int answer = -1;
//         while(start <= end){
//             int mid = (start + end) / 2;
//             if(nums[mid] == target){
//                 answer = mid;
//                 end = mid - 1;
//                 continue;
//             }

//             if(nums[mid] > target){
//                 end = mid - 1;
//                 continue;
//             }

//             if(nums[mid] < target){
//                 start = mid + 1;
//                 continue;
//             }
//         }
//         return answer;
//     }

//     int findHighEnd(vector<int>& nums,int &target){
//         int numsLength = nums.size();
//         int start = 0 , end = numsLength - 1;
//         int answer = -1;
//         while(start <= end){
//             int mid = (start + end) / 2;
//             if(nums[mid] == target){
//                 answer = mid;
//                 start = mid + 1;
//                 continue;
//             }

//             if(nums[mid] > target){
//                 end = mid - 1;
//                 continue;
//             }

//             if(nums[mid] < target){
//                 start = mid + 1;
//                 continue;
//             }
//         }
//         return answer;
//     }

//     vector<int> searchRange(vector<int>& nums, int target) {
//         int lowerEnd = findLowerEnd(nums,target);
//         int higherEnd = findHighEnd(nums,target);
//         return {lowerEnd,higherEnd};
//     }
// };
#pragma endregion