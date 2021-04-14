#include <numeric>
#include <vector>
#include <iostream>
#include <algorithm>
#define null NULL
#define all(i) i.begin(), i.end()

using namespace std;
#define p(x) cout<<x<<endl;

class Solution
{
public:
    vector<int> constructArray(int n, int k)
    {
        vector<int> v(n);
        iota(all(v),1);
        for_each(all(v),[](int i){printf("%d ", i);});
        cout<<endl;

        // as i grows, the reversable region shrinks
        for (int i = 1;i < k;++i)
        {
            reverse(v.begin()+i,v.end());
        }

        return v;
    }
};


#pragma region more optimized solution
// vector<int> constructArray(int n, int k) {
//         vector<int> res;
//         int i=1, j=n;
//         while(i <= j)
//         {
//             if(k > 1) res.push_back(k-- % 2 ? i++ : j--);
//             else res.push_back(i++);

//         }
//         return res;

//     }

#pragma endregion