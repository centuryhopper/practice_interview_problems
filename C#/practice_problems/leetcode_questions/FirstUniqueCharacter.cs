using System;
using System.Collections.Generic;

namespace practice_problems
{
    /*
    Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

    Examples:

    s = "leetcode"
    return 0.

    s = "loveleetcode"
    return 2.

    Note: You may assume the string contains only lowercase English letters.

    */
    public class FirstUniqueCharacter
    {
        void p(object m) => Console.WriteLine(m);


        public int FirstUniqChar(string s)
        {

            if (s == String.Empty || s == null) { return -1; }

            int l = s.Length;

            // store each character as a key and its freq as the value
            var d = new Dictionary<char, int>(l);

            for (int i = 0; i < l; ++i)
            {
                char ch = s[i];
            // p(ch);
                if (!d.ContainsKey(ch)) { d[ch] = 1; }
                else
                {
                    ++d[ch];
                }

                //p(d[ch]);
            }


            for (int i = 0; i < l; ++i)
            {
                char ch = s[i];
                if (d[ch] == 1) { return i; }
            }

            return -1;
        }
    }
}