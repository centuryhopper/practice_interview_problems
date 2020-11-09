#include <cstdint>
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <climits>
#include <iterator>
#include <functional>
#include <memory>
#define print(x) std::cout << x << std::endl;
#define null NULL
#define fl(i, k, n) for (int i = k; i < n; ++i)
using namespace std;


// g++ –std=c++17 [filename].cpp && ./a.out (type '–std=c++17' out manually. Don't copy
// & paste because the copy & pasted hyphen isn't recognized)

// OLD WAY:
// template<typename T>
// void ForEach(const vector<T>& vec, void(*func) (T))
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




// unique pointer (first preference that I should use)
// then shared and weak ptrs second preference


int	main(int argc, char **argv)
{
    // vector<int> a {1,2,3,4,10};
    // ForEach<int>(a, [](int elem) { print(elem); });

    // vector<std::string> b {"a", "b", "c", "d"};
    // ForEach<std::string>(b, [](std::string elem) { print(elem); });

    std::cout << std::boolalpha << std::endl;


    // unique_ptr<int[]> intAr = make_unique<int[]>(5);
    // unique_ptr<int[]> intAr(new int[5]);

    // int i;
    // fl(i, 0, 5)
    // {
    //     print(intAr[i]);
    // }

    // int i = 4;
    // int j = i++; // i = 5, j = 4
    // int k = ++j; // j = 5, k = 5
    // std::cout << i << j << k << std::endl;
    // int a, b;

    // cin >> a >> b;
    // print(a);
    // print(b);

    // int n = 5; void* p = &n;
    // int *pi = static_cast<int*>(p);
    // ++*pi;
    // print(*pi);

    int arr[] = {1, 2, 3, 4};
    int* p = arr;
    int* k = p;
    // std::cout << (*(k + 2) + 1[p] + *(0 + arr)) << std::endl;
    std::cout << 1[p] << " " << p[1] << std::endl;

    int8_t a = 200;
    uint8_t b = 100;
    if (a > b)
    {
        print("a");
    }
    else
    {
        print("b");
    }




    return 0;
}



