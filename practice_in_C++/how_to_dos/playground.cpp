#include <iostream>
#include <vector>
#include <algorithm>
#include <system_error>
#include <cstdio>
#include "../templates/template.h"

struct File
{
    File(const char *path, bool write)
    {
        auto file_mode = write ? "w" : "r";
        file_pointer = fopen(path, file_mode);
        if (!file_pointer)
            throw std::system_error(errno, std::system_category());
    }
    ~File()
    {
        fclose(file_pointer);
    }
    FILE *file_pointer;
};

template <typename T>
T add(T x, T y, T z)
{
    return x + y + z;
}
struct Foundation
{
    const char *founder;
};

struct Mutant
{
    // Constructor sets foundation appropriately:
    Mutant(std::unique_ptr<Foundation> foundation)
        : foundation(std::move(foundation)) {}
    std::unique_ptr<Foundation> foundation;
};


int main(void)
{
    // std::unique_ptr<Foundation> second_foundation{new Foundation};
    // // Access founder member variable just like a pointer:
    // second_foundation->founder = "Wanda";
    // cout<<second_foundation->founder<<endl;
    // std::unique_ptr<Foundation> second_foundation{new Foundation{}};
    // // ... use second_foundation
    // Mutant the_mule{std::move(second_foundation)};
    // second_foundation is in a 'moved-from' state
    // the_mule owns the Foundation

    // the square brackets initializes all values to 0
    int test[5]={};
    memset(test,-1,sizeof(test));
    for (int i = 0; i < 5; ++i)
        cout<<test[i]<<' ';
    nl;

#pragma region
// int ar[] = {1,2,3};

// for (int& i : ar)
// {
//     i = 0;
//     printf("%d\n", i);
// }

// // std sort
// std::vector<int> v{0, 1, 8, 13, 5, 2, 3};
// v[0] = 21;
// v.emplace_back(1);
// sortall(v);
// std::cout << "Printing " << v.size() << " Fibonacci numbers.\n";
// for (auto number : v)
// {
//     std::cout << number << " ";
// }
// cout<<endl;

// // lambdas
// auto cntOdds = std::count_if(all(v), [] (auto number) { return number & 1; });

// cout<<cntOdds<<endl;

// const std::size_t N = 10;
// int *a = new int[N];
// int *end = a + N;
// for (std::ptrdiff_t i = N; i > 0; --i)
// {
//     // cout<<*end << ' ' <<i<<endl;
//     // (*end) = *(end - i);
//     std::cout << (*(end - i) = i) << endl;
// }

// delete[] a;

// auto a = add(1, 2, 3);
// auto b = add(1L, 2L, 3L);
// auto c = add(1.F, 2.F, 3.F);
#pragma endregion

        return 0;
}
