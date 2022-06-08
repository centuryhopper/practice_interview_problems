#include<bits/stdc++.h>
using namespace std;

class Solution
{
    /*
    a:1, b:2, ... y:25, z:26

    n = 3, k = 27
    res: aaa
    while k > n:
        27 - 25 is not >= 3
        27 - 24 is >= 3
            so k -= 24
    res: aay


    n = 5, k = 73
    res = aaaaa
    73 - 25 is >= 5
    so res = aaaaz
    k = 73 - 25 = 48
    48 - 25 is >= 5
    so res = aaazz
    k = 48 - 25 = 23
    23 - 25 is not >= 5
    but 23 - 18 is >= 5
    so res = aaszz
    k = 23 - 18 = 5
    now since k == n
    we break out of the loop
    res: aaszz



    n=74657
    k=743771
    --- same idea ---

    */
public:
    string getSmallestString(int n, int k)
    {
        // populate with smallest possible string of size n
        string ans = "";
        for (int i = 0;i < n;i++)
        {
            ans += "a";
        }

        // go backwards
        int i = n-1;
        while (k > n)
        {
            int c = 25;
            c = (k-c) >= n ? c : k - n;
            ans[i--] = char(c+97);
            k -= c;
        }



        return ans;
    }
};