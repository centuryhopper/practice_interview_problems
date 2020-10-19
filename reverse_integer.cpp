#include <cstdint>
#include <iostream>
#include <thread>
#include <vector>
#include <atomic>
#include <chrono>
#include <string>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <climits>
#include <iterator>
#include <queue>
#include <sstream>
#define print(x) std::cout << x << std::endl
// using namespace std;

// g++ –std=c++17 [filename].cpp && ./a.out (type '–std=c++17' out manually. Don't copy
// & paste because the copy & pasted hyphen isn't recognized)

/*
Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Example 4:

Input: x = 0
Output: 0
*/


int reverse(int x)
{
    #pragma region edge cases


    // integer overflow checks
    if (x > INT32_MAX - 1 || x <= INT32_MIN)
    {
        return 0;
    }

    // single digits
    if (abs(x) / 10 == 0)
    {
        return x;
    }
    #pragma endregion

    bool isNeg = false;

    // force the input to be positive
    if (x < 0)
    {
        x = abs(x);
        isNeg = true;
    }

    std::queue<int> myQueue;

    while (x != 0)
    {
        // store trailing digit
        myQueue.push(x % 10);

        // chop trailing digit off
        x /= 10;
    }

    std::string res = "";

    while (!myQueue.empty())
    {
        res.append(std::to_string(myQueue.front()));
        myQueue.pop();
    }

    // remove leading zeros
    res.erase(0, res.find_first_not_of('0'));



    // convert back to int
    std::stringstream stream(res);

    // converts from string to int
    // if number is greater than int_max,
    // then truncates it to int_max
    stream >> x;


    if (x == INT32_MAX)
    {
        return 0;
    }

// back to negative
    if (isNeg)
    {
        x *= -1;
    }

    return x;
}

int main(int argc, char const *argv[])
{
    std::cout << std::boolalpha << std::endl;

    bool x = 1534236469 > INT32_MAX;
    print(x);

    print(reverse(1534236469));
    print(reverse(INT32_MAX));
    print(reverse(INT32_MIN));


    return 0;
}



// brute force solution failed with x = 1534236469
/*

void reverseChar(char* str)
{
    std::reverse(str, str + strlen(str));
}

int reverse(int x)
{
    #pragma region edge cases
    // integer overflow checks
    if (x > INT_MAX - 1 || x < INT_MIN)
    {
        return 0;
    }

    // single digits
    if (abs(x) / 10 == 0)
    {
        return x;
    }
    #pragma endregion


    bool isNeg = false;

    if (x < 0)
    {
        isNeg = true;
        x = abs(x);
    }

    // convert to string
    std::string value = std::to_string(x);

    // reverse the string
    char charArray[value.size() + 1];
    strcpy(charArray, value.c_str());

    reverseChar(charArray);

    // convert reversed char array back to string
    value = charArray;

    // remove leading zeros
    value.erase(0, value.find_first_not_of('0'));


    // convert back to int
    x = std::stoi(value);
    if (isNeg)
    {
        x *= -1;
    }

    // return the answer

    return x;
}

*/