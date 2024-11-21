#include <cstdint>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <climits>
#include <iterator>
#include <cctype>
#define print(x) std::cout << x << std::endl
using namespace std;

// g++ –std=c++17 [filename].cpp && ./a.out (type '–std=c++17' out manually. Don't copy
// & paste because the copy & pasted hyphen isn't recognized)

/*
Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
*/

class Solution
{
public:
    bool isPalindrome(string s)
    {
        int n = s.length();
        if (n <= 1)
            return true;

        int lo(0), hi(n - 1);

        while (lo < hi)
        {
            if (!isalnum(s[lo]))
            {
                ++lo;
            }
            else if (!isalnum(s[hi]))
            {
                --hi;
            }
            else
            {
                if (tolower(s[lo]) == tolower(s[hi]))
                {
                    ++lo;
                    --hi;
                }
                else
                {
                    return false;
                }
            }
        }
        return true;
    }
};

int main(int argc, char const *argv[])
{
    std::cout << std::boolalpha << std::endl;

    Solution sol = Solution();
    // print(sol.isPalindrome("racecar"));
    // print(sol.isPalindrome("bob"));
    // print(sol.isPalindrome("hey"));
    print(sol.isPalindrome("A man, a plan, a canal: Panama"));
    print(sol.isPalindrome("race a car"));
    print(sol.isPalindrome(".,"));

    return 0;
}
