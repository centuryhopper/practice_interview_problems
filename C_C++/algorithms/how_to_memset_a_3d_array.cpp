// Example program
#include <iostream>
#include <string>
#include <cstring>
using namespace std;
int main()
{
    int m=5,n=4;
    int*** memo = new int**[m+1];
    for (int i = 0; i <=m; ++i)
    {
        memo[i] = new int*[n+1];
        for (int j=0;j<=n;++j)
        {
            memo[i][j] = new int[3];
            memset(memo[i][j], -1, sizeof(memo[i][j])*3);
            // for (int k = 0;k<4;++k)
            // {
            //     memo[i][j][k] = -1;
            // }
        }
    }
    for(int i = 0;i <= m; ++i)
    {
        for (int j = 0;j <= n; ++j)
        {
            for (int k = 0;k<3;++k)
            {
                cout << memo[i][j][k] << " ";
            }
            cout << "\n";
        }
        cout << "\n\n";
    }
    cout << "\n";

  // clean up
    for(int i = 0;i <= m; ++i)
    {
        for (int j = 0;j <= n; ++j)
        {
            // free each 1-d array
            delete[] memo[i][j];
        }
        // then free that 2d array containing those freed 1-d arrays
        delete[] memo[i];
    }
    // finally delete the entire 3d array
    delete [] memo;
}
