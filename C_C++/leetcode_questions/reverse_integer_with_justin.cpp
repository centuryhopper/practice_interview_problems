#include <cstdint>
#include <iostream>
#include <cassert>
#include <string>
#define print(x) std::cout << x << std::endl
using namespace std;

// g++ –std=c++17 [filename].cpp && ./a.out (type '–std=c++17' out manually. Don't copy
// & paste because the copy & pasted hyphen isn't recognized)

// Mock interview (Justin Hawtree interviewed Leo Zhang on 10/14/2020 from 7pm - 9pm)


// input constraints: -2^31 <= x <= (2^31) - 1
int reverse(int x)
{
    // check bounds
    if (x <= INT32_MIN || x >= INT32_MAX)
    {
        return 0;
    }

    // remember whether the integer is negative or positive
    bool isNeg = false;
    if (x < 0)
    {
        isNeg = true;
        x *= -1;
    }

    // make sure the accumulator
    // won't have int32 integer overflow
    u_int64_t sum = 0;
    while (x > 0)
    {
        // multiply by 10 every time so the math works
        // for example 123 => (((((0 * 10) + 3) * 10) + 2) * 10) + 1 = 321
        sum *= 10;
        sum += (x % 10);
        x /= 10;
    }

    // upper bound check
    if (sum >= INT32_MAX)
    {
        return 0;
    }

    // lower bound check
    if (isNeg)
    {
        sum *= -1;
        if (sum < INT32_MIN)
        {
            return 0;
        }
    }

    return sum;
}



int main(void)
{
    std::cout << std::boolalpha << std::endl;

    // print(reverse(-123));
    // print(sizeof(int));
    // print(sizeof(int32_t));
    // print(sizeof(int64_t));

    // print(INT32_MAX);
    // print(INT32_MIN);

    assert(reverse(-134961997) == -799169431);
    assert(reverse(2058634571) == 1754368502);

    assert(reverse(-1788351638) == 0);
    assert(reverse(-1517915919) == 0);

    assert(reverse(1156187925) == 0);
    assert(reverse(-1729298266) == 0);
    assert(reverse(951174107) == 701471159);
    assert(reverse(1279383423) == 0);
    assert(reverse(-2037046622) == 0);

    print("hooray! All test cases passed!");

    return 0;
}





