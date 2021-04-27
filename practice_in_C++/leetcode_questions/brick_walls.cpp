#include "../templates/template.h"

class Solution
{

public:
    int leastBricks(vvi& walls)
    {
        unordered_map<int,int> m;
        for (auto wall : walls)
        {
            int curSum = 0;
            for (auto it=wall.begin();it!=wall.end()-1;++it)
            {
                curSum += *it;
                m[curSum] = m.find(curSum) != m.end() ? m[curSum] + 1 : 1;
            }
        }

        // cout<<"here"<<endl;
        // for (auto p : m) cout<<p.first<<','<<p.second<<' ';
        vector<int> values(m.size());
        transform(all(m),values.begin(),[](auto pair){return pair.second;});

        return m.empty() ? walls.size() :  walls.size() - *max_element(all(values));
    }

};


    auto speedup = []() {
    std::ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return nullptr;
}();
static const auto io_sync_off = []() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    return 0;
}();














#pragma region failed attempt
/**

#define vvi vector<vector<int>>
#define all(v) v.begin(),v.end()
class Solution
{

private:
//     int countMinBricks(const vvi& walls)
//     {
//         int cntTopEdge = 0;
//         int firstRowWidth = walls[0].size();
//         unordered_map<int,int> firstRow;
//         for (int i = 0;i < firstRowWidth;++i)
//             firstRow[walls[0][i]] = i;
//         // try cutting each brick in the first row
//         for (const auto& brickToCut : walls[0])
//         {
//             int indexOfInterest = firstRow[brickToCut];
//             for (int i = 1;i < walls.size();++i)
//             {
//                 if (walls[i].size() <= indexOfInterest)
//                     ++cntTopEdge;
//                 else if (walls[i][indexOfInterest] > brickToCut)
//                     ++cntTopEdge;
//             }
//         }

//         return cntTopEdge;
//     }

public:
    int leastBricks(vvi& walls)
    {
        // int oneWay = countMinBricks(walls);
        // reverse(all(walls));
        // int otherWay = countMinBricks(walls);
        // return min(oneWay, otherWay);
    }
};
 */
#pragma endregion