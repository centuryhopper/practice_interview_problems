#include <iostream>
#include <string>
#include <algorithm>
#include <array>
#include <vector>
#include <map>
#include <set>
#define p(x) std::cout << x << std::endl;
#define fl(i, k, n) for (int i = k; i < n; ++i)
#define null NULL
using namespace std;

class Solution
{
private:
    template <typename Map>
    bool key_compare(Map const &lhs, Map const &rhs)
    {
        return lhs.size() == rhs.size() && std::equal(lhs.begin(), lhs.end(), rhs.begin(),
                                                      [](auto a, auto b) { return a.first == b.first; });
    }

public:
    bool isAnagram(string s, string t)
    {
        int i;
        set<string> sSet(s.begin(), s.end()), tSet(t.begin(), t.end());
        map<string, size_t> sMap, tMap;
        for (string val : sSet)
        {
            sMap[val] = count(s.begin(), s.end(), val);
        }

        for (string val : tSet)
        {
            tMap[val] = count(t.begin(), t.end(), val);
        }

        return key_compare(sMap, tMap);
    }
};

int main(int argc, char const *argv[])
{
    auto s = Solution();

    p(s.isAnagram("leo", "lleo"));
    return 0;
}
