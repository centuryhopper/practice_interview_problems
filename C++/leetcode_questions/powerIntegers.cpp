#include "../templates/template.h"


class Solution
{
public:

    // find all powers of x and y less than bound
    vector<int> powerfulIntegers(int x, int y, int bound)
    {
        // get upper bounds for x power and y power
        int xub = x < 2 ? x : ceil(log(bound) / log(x)), yub = y < 2 ? y : ceil(log(bound) / log(y));

        // vector<int> xVec, yVec;
        // xVec.reserve(xub);yVec.reserve(yub);
        int xVec[xub];
        int yVec[yub];

        for (int i = 0;i < xub;++i) xVec[i] = pow(x,i);
        for (int i = 0;i < yub;++i) yVec[i] = pow(y,i);

        unordered_set<int> ret;
        for (int i = 0; i < xub;++i)
        {
            for (int j = 0;j < yub;++j)
            {
                if (xVec[i] + yVec[j] <= bound) ret.insert(xVec[i] + yVec[j]);
            }
        }

        return vector<int>(all(ret));
    }
};