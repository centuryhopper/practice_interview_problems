#include <iostream>
#include <vector>
#include <set>

#define p(x) std::cout << x << std::endl;
#define fl(i, k, n) for (int i = k; i < n; ++i)
#define null NULL
using namespace std;

class Solution
{
public:
    int distributeCandies(vector<int> &candyType)
    {
        set<int> s(candyType.begin(), candyType.end());
        return min(candyType.size() / 2, s.size());
    }
};

// slightly faster solution
// class Solution
// {
// public:
//     int distributeCandies(vector<int> &candyType)
//     {
//         int possible = candyType.size() / 2;

//         bitset<200001> types(0);

//         for (auto type : candyType)
//         {
//             types.set(type + 100000);
//         }

//         int typesNumber = types.count();

//         return typesNumber < possible ? typesNumber : possible;
//     }
// };