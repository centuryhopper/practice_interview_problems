using System;
using System.Collections.Generic;

public class FindDisappearedNumbers
{
    public IList<int> findDisappearedNumbers(int[] nums)
    {
        Array.Sort(nums);
        int n = nums.Length;

        var lst = new List<int>();

        for (int i = 0; i < n; ++i)
        {
            int currentNum = nums[i];
            int tmp = Math.Abs(currentNum) - 1;

            // force a negative value on to nums[tmp]
            nums[tmp] = Math.Abs(nums[tmp]) * -1;
        }

        for (int i = 0; i < n; ++i)
        {
            if (nums[i] > 0)
            {
                lst.Add(i + 1);
            }
        }

        return lst;

    }
}
