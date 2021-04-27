using System;
using System.Collections.Generic;

namespace practice_problems
{
    public class LongestSubStringWithKRepeatingCharacters
    {
        public int LongestSubstring(string s, int k)
        {
            int n = s.Length;

            // check edge cases:
            if (String.IsNullOrEmpty(s) || n < k) { return 0; }

            // initialize map with all lowercase alphabetical letters
            Dictionary<char, int> d = new Dictionary<char, int>();
            for (char l = 'a'; l <= 'z'; ++l)
            {
                d[l] = 0;
            }

            // fill the map up with counts
            foreach (char c in s)
            {
                ++d[c];
            }

            // check if the whole input string is the answer
            bool allLettersIntheWordRepeatKTimes = true;
            foreach (char c in s)
            {
                if (d[c] < k && d[c] > 0)
                {
                    allLettersIntheWordRepeatKTimes = false;
                }
            }

            if (allLettersIntheWordRepeatKTimes) { return n; }

            int result = 0, start = 0, cur = 0;

            while (cur < n)
            {
                char c = s[cur];
                int numOccurencesForTheGivenLetter = d[c];

                // separation letters
                if (numOccurencesForTheGivenLetter > 0 && numOccurencesForTheGivenLetter < k)
                {
                    result = Math.Max(result, LongestSubstring(s.Substring(start, cur - start), k));
                    start = cur + 1;
                }

                ++cur;
            }

            result = Math.Max(result, LongestSubstring(s.Substring(start), k));


            return result;
        }
    }
}

