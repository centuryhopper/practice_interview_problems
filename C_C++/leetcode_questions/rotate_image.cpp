#include "../templates/template.h"

#define vvi vector<vector<int>>
#define deb(x) cout << #x << " = " << x << ", "
#define all(x) x.begin(), x.end()
#define p(v) for_each(all(v), [](auto e) { cout<<e<<" "; })
#define nl cout<<endl;

class Solution
{
// private:
//     void swap(vvi& mat, int i, int j)
//     {
//         int tmp = mat[i][j];
//         mat[i][j] = mat[j][i];
//         mat[j][i] = tmp;
//     }

public:
    void rotate(vector<vector<int>>& mat)
    {
        int n = mat.size();

        // transpose (A[i][j] = A[j][i]) then reverse the row
        for (int i = 0;i < n;++i)
        {
            for (int j = i; j < n;++j)
            {
                swap(mat[i][j], mat[j][i]);
            }
            reverse(all(mat[i]));
        }
    }
};

















// failed attempt
// class Solution
// {
// private:
//     void swap(vvi& mat, int rowIndex, int colIndex, int* cache, int cacheIndex)
//     {
//         int tmp = mat[rowIndex][colIndex];
//         mat[rowIndex][colIndex] = cache[cacheIndex];
//         cache[cacheIndex] = tmp;
//     }

// public:
//     void rotate(vector<vector<int>>& mat)
//     {
//         int m = mat.size(),n = mat[0].size();
//         int cache[n];

//         for (int i = 0; i < n; ++i){ cache[i] = mat[0][i]; }

//         int lb = 0, ub = n-1;
//         while (lb < ub)
//         {
//             // topmost row
//             for (int i = 0; i < n-1;++i)
//             {
//                 mat[0][i] = mat[n-1-i][0];
//             }
//             mat[0][n-1] = cache[0];

//         // for(auto v:mat) { p(v);nl; }
//         // for (auto i : cache){ deb(i);}
//         // nl;

//             // right most col
//             for (int i = 1; i < n;++i)
//             {
//                 swap(mat,i,n-1,cache,i);
//             }
//         // for(auto v:mat) { p(v);nl; }
//         // for (auto i : cache){ deb(i);}
//         // nl;

//             // bottom most row
//             for (int i=n-2,j=1;i >= 0;--i,++j)
//             {
//                 swap(mat,n-1,i,cache,j);
//             }

//         // for(auto v:mat) { p(v);nl; }
//         // for (auto i : cache){ deb(i);}
//         // nl;

//             // left most col
//             for (int i = n-2,j=1; i > 0;--i,++j)
//             {
//                 swap(mat,i,0,cache,j);
//             }
//             for(auto v:mat) { p(v);nl; }
//             for (auto i : cache){ deb(i);}
//             nl;

//             ++lb;--ub;
//         }


//     }
// };