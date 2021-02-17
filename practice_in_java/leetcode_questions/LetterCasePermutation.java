package leetcode_questions;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class LetterCasePermutation
{
    HashSet<String> sett = new HashSet<String>();

    void permute(char[] lst, int l, int r)
    {
        if (l > r)
        {
            String s = String.valueOf(lst);
            if (!sett.contains(s))
            {
                sett.add(s);
            }
            return;
        }
        for (int i = l; i <= r; ++i)
        {
            lst[i] = Character.toUpperCase(lst[i]);
            String s = String.valueOf(lst);
            if (!sett.contains(s))
                permute(lst, l + 1, r);

            lst[i] = Character.toLowerCase(lst[i]);
            s = String.valueOf(lst);
            if (!sett.contains(s))
                permute(lst, l + 1, r);
        }
    }

    public List<String> letterCasePermutation(String s)
    {
        var charAr = s.toCharArray();
        permute(charAr, 0, s.length() - 1);
        var ret = new ArrayList<String>(sett);
        sett.clear();
        return ret;
    }
}
