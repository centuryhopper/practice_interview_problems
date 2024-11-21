#include <iostream>
#include <vector>
#include <algorithm>
#define all(itr) itr.begin(), itr.end()

using namespace std;

void print_even(int n)
{
    if (n % 2 == 0)
        cout << n << ' ';
}

int main(void)
{
    vector<int> v = {1, 2, 3, 4, 5};
    cout << "Vector contains following even numebr" << endl;
    for_each(all(v), [](int n) { return n % 2 == 0 ? printf("%d ", n) : printf(""); });
    cout << endl;
    return 0;
}
