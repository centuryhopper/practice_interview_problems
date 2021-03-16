// Example program
#include <iostream>
#include <string>
#include <memory>
#include <functional>
using namespace std;

class hello
{
public:
    int value = 10;
};

// pass by value example
void pbv(hello h)
{
    h.value = 50;
}

// pass by reference example
void pbr(hello &h, int newVal = 100)
{
    h.value = newVal;
}

void pb(hello* h, int newVal = 100)
{
    h->value = newVal;
}

int maxi(int a, int b) { return a > b ? a : b; }

int main()
{
    auto hi = hello();
    printf("%d\n", hi.value);
    pbv(hi);
    printf("%d\n", hi.value);

    // int (*f) (int, int);
    // f = &maxi;
    // std::function<int(int, int)>
    auto f = [](int a, int b) { return a > b ? a : b; };

    pbr(hi);
    printf("after pass by reference: %d\n", f(hi.value, 500));

    auto h = make_unique<hello>(new hello());
    pb(h.get(), 1200);
    printf("after pass by reference of smartpointer: %d\n", f(hi.value, 1000));

    //   std::string name;
    //   std::cout << "What is your name? ";
    //   getline (std::cin, name);
    //   std::cout << "Hello, " << name << "!\n";
}
