#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

#define all(itr) itr.begin(), itr.end()

using namespace std;

int main(void)
{
    vector<int> v = {1, 2, 3, 4, 5};
    vector<int> vout;
    // transform(all(v), back_inserter(v), [](int& val) { return val * 3; });
    transform(all(v), v.begin(), [](int& val) { return val * 3; });

    for_each(all(v), [](int n) { printf("%d ", n); });
    cout << endl;

    auto endFilter = remove_if(all(v), [](int n)
    {
        return n % 2 == 1;
    });

    v.erase(endFilter, v.end());

    // print out all even numbers left in the list
    for_each(v.begin(), endFilter, [](int n) { printf("%d ", n); });
    cout << endl;

    for_each(all(v), [](int n) { printf("%d ", n); });
    cout << endl;

    int acc = accumulate(all(v), 0, [](int first, int second) {return first + second;});

    printf("%d\n", acc);

    cout << endl;
    return 0;
}
