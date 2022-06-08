using System;

namespace practice_problems
{
    public static class ArrayProblems
    {

        #region Rotate Array
//         Example 1:

// Input: nums = [1,2,3,4,5,6,7], k = 3
// Output: [5,6,7,1,2,3,4]
// Explanation:
// rotate 1 steps to the right: [7,1,2,3,4,5,6]
// rotate 2 steps to the right: [6,7,1,2,3,4,5]
// rotate 3 steps to the right: [5,6,7,1,2,3,4]

// Example 2:

// Input: nums = [-1,-100,3,99], k = 2
// Output: [3,99,-1,-100]
// Explanation:
// rotate 1 steps to the right: [99,-1,-100,3]
// rotate 2 steps to the right: [3,99,-1,-100]



// Constraints:

//     1 <= nums.length <= 2 * 104
//     -231 <= nums[i] <= 231 - 1
//     0 <= k <= 105

        public static void Rotate(int[] nums, int k)
        {
            int n = nums.Length;
            k %= n;

            if (k == 0 || n == 1) { return; }


            Array.Reverse(nums);

            Array.Reverse(nums, 0, k);

            Array.Reverse(nums, k, n - k);

        }
        #endregion

        

    }
}