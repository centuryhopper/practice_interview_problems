class Solution
{

// 0 1 1 2 3 5 8 13 21 ...

public:
    int fib(int n)
    {
        if (n < 2) return n;
        int a = 0, b = 1;
        int c;
        for (int i=2;i<=n;++i)
        {
            c = a+b;
            a = b;
            b = c;
        }
        return c;

    }
};

#pragma O(1) solution
/**
 class Solution
{

// 0 1 1 2 3 5 8 13 21 ...

public:
    int fib(int n)
    {
        float goldenRatio = (1+sqrt(5))/2;
        return static_cast<int>(round(pow(goldenRatio,n) / sqrt(5)));
    }
};
 */
#pragma endregion