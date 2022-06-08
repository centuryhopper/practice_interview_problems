#include "../templates/template.h"


// keep xoring and (and-bitshift left) until y is exhausted to 0
long long add(long long x, long long y)
{
    if (y == 0) return x;

    return add(x^y, (x&y)<<1);
}


int main(void)
{
    cout<< add(1000000,1000000) <<endl;

    return 0;
}

