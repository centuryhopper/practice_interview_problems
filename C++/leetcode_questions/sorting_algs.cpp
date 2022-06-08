#include <cstdint>
#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <climits>
#include <iterator>
#include <array>
#include <vector>
#include <map>
#include <set>
#include <tuple>
#include <stack>
#include <queue>
#define print(x) std::cout << x << std::endl;
#define fl(i, k, n) for (int i = k; i < n; ++i)
using namespace std;


class sorting_algs
{
    private:
        void Swap(int array[], int i, int j);
    public:
        int x;
        sorting_algs(/* args */);
        ~sorting_algs();



        void QuickSort(int* array)
        {

        }
};

void sorting_algs::Swap (int array[], int i, int j) { int tmp = array[i]; array[i] = array[j]; array[j] = tmp; }


sorting_algs::sorting_algs(/* args */)
{
}

sorting_algs::~sorting_algs()
{
}

int main(int argc, char const *argv[])
{
    sorting_algs s;

    int x;
    print("x is " + to_string(x));

    print("obj x is " + to_string(s.x));
    return 0;
}



