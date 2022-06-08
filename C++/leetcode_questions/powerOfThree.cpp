

class Solution
{
public:
    bool isPowerOfThree(int n)
    {
        // n should be a natural number and be divisible by the biggest integer less than int_max
        // return (n > 0 && 1162261467 % n == 0);
        return rec(n);
    }
private:
    // recursive
    bool rec(double n)
    {
        if (n < 1) return false;
        // 3^0 == 1
        if (n == 1) return true;
        return rec(n/3);
    }
};