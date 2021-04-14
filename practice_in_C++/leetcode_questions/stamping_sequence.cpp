#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;


class Solution
{

private:
    // if true, then we will do target.replace(i, stamp.length(), "?");
    // offset will have us compare the correct substring in the targetSubstring
    // int canReplace(string stamp, int offset, string targetSubStr)
    // {
    //     for (int i = 0; i < stamp.length(); ++i)
    //     {
    //         if (targetSubStr[i] == '?') continue;
    //         if (stamp[i] != targetSubStr[i]) return false;
    //     }
    //     return true;
    // }

    bool canReplace(char* stamp, int offset, int stampLen, char* target)
    {
        for (int i = 0; i < stampLen; ++i)
        {
            if (target[i+offset] == '?') continue;
            if (stamp[i] != target[i+offset]) return false;
        }
        return true;
    }

    void replace(char* target, int offset, int stampLen, int& cnt)
    {
        for (int i = 0; i < stampLen; ++i)
        {
            if (target[i+offset] != '?')
            {
                target[i+offset] = '?';
                ++cnt;
            }
        }
    }
public:
    vector<int> movesToStamp(string stamp, string target)
    {
        // check if stamp exists as a substring in target,
        // if it does, replace that substring with all ?
        // if it doesn't exist, then return empty array

        // find index of first occurrance of substring stamp
        size_t found = target.find(stamp);
        if (found > target.length() || found < 0) return {};

        int t = target.length(), s = stamp.length();

        // +1 to account for the null character at the end
        char tChar[t+1], sChar[s+1];
        strcpy(tChar, target.c_str());
        strcpy(sChar, stamp.c_str());

        // start off by changing part of the target string that matches
        // the stamp with all asterisks
//         string substitute(stamp.length(), "*");
//         target.replace(found, stamp.length(), substitute);

        vector<int> res;
        int cnt = 0;
        bool visited[t];
        for (int i = 0; i < t; ++i)
            visited[i] = false;

        // to avoid out of bounds error for the target length
        int diff = t - s;

        // keep going until we have all asterisks
        while (cnt != t)
        {
            bool didChange = false;
            for (int i = 0; i <= diff; ++i)
            {
                if (!visited[i] && canReplace(sChar, i, s, tChar))
                {
                    replace(tChar, i, s, cnt);
                    visited[i] = true;
                    didChange = true;
                    res.emplace_back(i);

                    if (cnt == t) break;
                }
            }

            if (!didChange) return {};
        }

        reverse(res.begin(), res.end());


        return res;
    }
};























#pragma region more optimized solution
// class Solution {
// private:
//     bool match(string& stamp, string& target, int index) {
//         int m = stamp.size(), count = 0;
//         for (int i=0; i<m; ++i) {
//             if (target[index+i]=='?') continue;
//             else if (target[index+i]==stamp[i]) count++;
//             else return false;
//         }
//         return count>=1;
//     }
// public:
//     vector<int> movesToStamp(string stamp, string target) {
//         int n = target.size(), m = stamp.size();
//         vector<int> result;
//         for (int i=0; i<=n-m; ++i) {
//             if (match(stamp, target, i)) {
//                 result.push_back(i);
//                 fill(target.begin()+i, target.begin()+i+m, '?');
//             }
//         }
//         reverse(target.begin(), target.end());
//         reverse(stamp.begin(), stamp.end());
//         for (int i=0; i<=n-m; ++i) {
//             if (match(stamp, target, i)) {
//                 result.push_back(n-m-i);
//                 fill(target.begin()+i, target.begin()+i+m, '?');
//             }
//         }
//         for (auto ch : target) {
//             if (ch!='?') return {};
//         }
//         reverse(result.begin(), result.end());
//         return result;
//     }
#pragma endregion