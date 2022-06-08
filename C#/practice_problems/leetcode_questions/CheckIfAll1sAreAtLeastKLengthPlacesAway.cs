using System.Collections.Generic;

public class CheckIfAll1sAreAtLeastKLengthPlacesAway
{
    public bool KLengthApart(int[] nums, int k)
    {
        var l = new List<int>(nums.Length);

        for (int i = 0; i < nums.Length; ++i)
        {
            if (nums[i] == 1)
            {
                l.Add(i);
            }
        }

        if (l.Count > 1)
        {
            for (int j = 1; j < l.Count; ++j)
            {
                if ((l[j] - l[j-1]) - 1 < k)
                {
                    return false;
                }
            }
        }

        return true;
    }
}