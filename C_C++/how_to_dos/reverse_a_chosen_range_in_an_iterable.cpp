// Example program
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    //   std::string name;
    //   std::cout << "What is your name? ";
    //   getline (std::cin, name);
    //   std::cout << "Hello, " << name << "!\n";
    vector<int> v{1,2,3,4,5};
    reverse(v.begin()+1,v.end());
    for_each(v.begin(),v.end(),[](int i){printf("%d ", i);});
    cout<<endl;
}
