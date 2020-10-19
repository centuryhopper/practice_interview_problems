#include <cstdint>
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <climits>
#include <iterator>
#include <functional>
#define print(x) std::cout << x << std::endl;
#define fl(i, k, n) for (int i = k; i < n; ++i)
using namespace std;
// g++ –std=c++17 [filename].cpp && ./a.out (type '–std=c++17' out manually. Don't copy
// & paste because the copy & pasted hyphen isn't recognized)

// OLD WAY:
// template<typename T>
// void ForEach(const vector<T>& vec, void(*func) (int))
// {
//     for(int elem : vec)
//     {
//         func(elem);
//     }
// }

// NEW WAY using macros:

// prints each element in the vector container
template<typename T>
void ForEach(const vector<T>& vec, void(*f)(T))
{
    int i, n = vec.size();
    fl(i, 0, n)
    {
        print(vec[i]);
    }
}





int	main(int argc, char **argv)
{
    // vector<int> a {1,2,3,4,10};
    // ForEach<int>(a, [](int elem) { print(elem); });

    // vector<std::string> b {"a", "b", "c", "d"};
    // ForEach<std::string>(b, [](std::string elem) { print(elem); });

    




    return 0;
}



