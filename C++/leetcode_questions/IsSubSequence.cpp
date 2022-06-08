#include<bits/stdc++.h>


class Solution
{

    /*
    */


public:
    bool isSubsequence(std::string s, std::string t)
    {
        int sl = s.length(), tl = t.length();
        if (sl > tl) return false;

        int cur = 0;

        for (int i=0;i<tl;i++)
        {
            // move cur along s and bound it by the length of s
            if (s[cur] == t[i])
            {
                cur = std::min(sl,cur+1);
            }
        }

        return cur == sl;
    }
};