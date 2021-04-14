// Example program
#include <iostream>
#include <string>
#include <cstring>
#include <stdio.h>

int main()
{
    // fill entire array with -1's
    // will only work with either 0 or -1
    int dp[5][5];
    printf("size of array: %d\n", sizeof(dp));
    memset(dp, -1, sizeof(dp));
    for (int i = 0; i < 5;++i)
    {
        for (int j = 0;j < 5;++j)
        {
            printf("%d ", dp[i][j]);
        }
        printf("\n");
    }
}
