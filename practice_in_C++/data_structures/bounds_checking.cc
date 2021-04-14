// Example program
#include <iostream>
#include <string>
#include <stdexcept>

struct BoundsCheckingContainer
{
public:
    int* a;
    int size;
    BoundsCheckingContainer(int* array, int len) :a(array), size(len)
    {}

    // lvalue sign => &
    // without it, we can't write to it
    int& operator[](int i)
    {
        if (i >= size || i < 0)
        {
            std::cout << "index out of bounds" << "\n";
            throw std::invalid_argument("index out of bounds");
        }
        return a[i];
    }
};

int main()
{

    int a[] = {1,2,3};
    int size = sizeof(a) / sizeof(int);
    struct BoundsCheckingContainer ar(a,size);
    ar[0] = 7;

    for (int i = 0; i < size+1;++i)
    {
        std::cout << ar[i] << "\n";
    }
}
