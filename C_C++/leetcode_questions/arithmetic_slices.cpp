#include <vector>
#define p(x) std::cout << x << std::endl;
#define fl(i, k, n) for (int i = k; i < n; ++i)
#define null NULL
using namespace std;


class Solution
{
public:

    int numberOfArithmeticSlices(vector<int>& a)
    {
        if (a.size() < 3) return 0;

        int retSum = 0, i = 2, diff = a[i-2] - a[i-1], rate = 1;
        while (i < a.size())
        {
            if (diff == a[i-1] - a[i])
            {
                retSum += rate;
                ++rate;
            }
            else
            {
                rate = 1;
                diff = a[i-1] - a[i];
            }

            ++i;
        }

        return retSum;

    }
};