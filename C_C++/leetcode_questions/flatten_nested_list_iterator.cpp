
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
#include "../templates/template.h"


class NestedIterator
{
private:
    vector<int> tmp;
    // number of integers in the nested list
    int i = 0;


public:
    NestedIterator(vector<NestedInteger> &nestedList)
    {
        for (auto& i : nestedList)
        {
            rec(i);
        }
        // cout<<"there are "<<cnt<<" integers in the nested list"<<endl;
        p(tmp);
    }

    // [[1,1],2,[1,1]]
    // [1,[4,[6]]]
    // recursively get all integers in the nested list
    void rec(const NestedInteger& ni)
    {
        if (ni.isInteger())
        {
            // cout<<lst[i].getInteger()<<' ';
            tmp.eb(ni.getInteger());
        }
        else
        {
            auto v = ni.getList();
            for (auto l : v)
            {
                rec(l);
            }
        }
    }


    int next()
    {
        return tmp[i++];
    }

    bool hasNext()
    {
        return i < tmp.size();
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */




#pragma region online optimized solution
// class NestedIterator {
// public:
//     vector<int> list;
//     int i;

//     void flattenList(vector<NestedInteger> &nestedList, int i) {
//         if (i == nestedList.size())
//             return;
//         if (nestedList[i].isInteger()) {
//             list.push_back(nestedList[i].getInteger());
//         } else {
//             flattenList(nestedList[i].getList(), 0);
//         }
//         flattenList(nestedList, i + 1);
//     }

//     NestedIterator(vector<NestedInteger> &nestedList) {
//         i = 0;
//         flattenList(nestedList, 0);
//     }

//     int next() {
//         return list[i++];
//     }

//     bool hasNext() {
//         if (i == list.size())
//             return false;
//         return true;
//     }
// };
#pragma endregion
