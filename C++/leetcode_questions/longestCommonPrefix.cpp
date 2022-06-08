#include "templates/template.h"

// time: O(n) checking every pair of strings and, in the worst case, comparing each character for every comparison
// space: O(n) because we create an array to cache the results
class Solution
{

private:
    int getLCP(string a, string b)
    {
        int len = min(a.size(), b.size());
        int cnt = 0;

        // loop the size of the smaller string
        for (int i=0;i<len;++i)
        {
            // if they match keep going
            // otherwise no point in continuing the loop
            if (a[i] == b[i])
                ++cnt;
            else
                break;
        }

        return cnt;
    }


public:
    string longestCommonPrefix(vector<string>& strs)
    {
        // edge case
        if (strs.size() == 1) return strs[0];

        // create lcp array
        vector<int> lcp(strs.size(), 0);
        for (int i = 1;i<strs.size();++i)
        {
            lcp[i] = getLCP(strs[i-1], strs[i]);
        }

        // minimum because for example:
        /*
            for the input: ["flower","flow","flight"], we have the lcp array [0, 4, 2]
            and we don't count the first element in lcp because it's just a place holder, so
            we're left with 4 and 2 and we pick 2 because the answer is 'fl', which is correct.
            If we picked 4, then the answer is 'flow', which is incorrect because there's no
            'flow' as a prefix in 'flight'
        */
        int longestprefixlen = *min_element(lcp.begin()+1,lcp.end());
        // for (auto i:lcp)
        //     cout<<i<<' ';
        // cout<<endl;

        return strs[0].substr(0,longestprefixlen);
    }
};