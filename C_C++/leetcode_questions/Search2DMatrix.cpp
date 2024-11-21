#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    /*
    start at the last element in the first row and go either left or down depending on the current value compared to the target value
    */
    bool searchMatrix(vector<vector<int>>& matrix, int target)
    {
        int i = 0, j = matrix[0].size() - 1;
        while (i < matrix.size() && j >= 0)
        {
            int cur = matrix[i][j];
            if (cur == target) return true;

            if (cur > target) j--;
            else i++;
        }
        return false;
    }
};