#include<bits/stdc++.h>

class Solution
{
    /*
    b c a b c

    c b a c d c b c

    a c d b

    c b a c d c b c

    a c d b

    "ecbacba"

    "cbac"

    "ccacbaba"
    */
public:
    std::string removeDuplicateLetters(std::string s)
    {
        int d[26];
        memset(d, -1, sizeof(d));
        // for (int i=0;i<26;i++) cout<<dict[i]<<" ";
        int n = s.length();
        // int visited = 0;
        std::string ans = "";
        // get last seen values of each character
        for (int i = n-1;i>=0;i--)
        {
            int asciiIndex = s[i] - 'a';
            if (d[asciiIndex] == -1)
            {
                d[asciiIndex] = i;
            }
        }
        for (int i=0;i<n;i++)
        {
            // cout<<ans<<"\n";
            int asciiIndex = s[i] - 'a';
            char cur = s[i];
            if (ans.empty())
            {
                ans+=cur;
            }
            else if (cur < ans.back() && d[ans.back() - 'a'] != -1 && ans.find(cur) == std::string::npos)
            {
                while (!ans.empty() && cur < ans.back() && d[ans.back() - 'a'] != -1)
                    ans.pop_back();
                ans+=cur;
            }
            // last occurrance
            else if (d[asciiIndex] == i && ans.find(cur) == std::string::npos)
            {
                d[asciiIndex] = -1;
                ans+=cur;
            }
            else if (ans.find(cur) == std::string::npos)
            {
                ans+=cur;
            }

            // mark as such if this is the last occurrance
            if (d[asciiIndex] == i) d[asciiIndex] = -1;



        }

        return ans;
    }
};

