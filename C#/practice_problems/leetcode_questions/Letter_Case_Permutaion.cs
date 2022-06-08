using System;
using System.Collections.Generic;

namespace practice_problems
{
    public class Letter_Case_Permutation
    {
        HashSet<string> sett = new HashSet<string>();

        void Permute(char[] lst, int l, int r)
        {
            if (l >= r)
            {
                sett.Add(string.Join("", lst));
                return;
            }
            for (int i = l; i < r; ++i)
            {
                // Console.WriteLine(i);
                lst[i] = Char.ToUpper(lst[i]);
                string s = string.Join("", lst);
                if (!sett.Contains(s))
                    Permute(lst, l + 1, r);

                lst[i] = Char.ToLower(lst[i]);
                s = string.Join("", lst);
                if (!sett.Contains(s))
                    Permute(lst, l + 1, r);
            }
        }

        public List<string> LetterCasePermutation(string s)
        {
            var charAr = s.ToCharArray();
            Permute(charAr, 0, s.Length);
            var ret = new List<string>(sett);
            sett.Clear();
            return ret;
        }
    }
}