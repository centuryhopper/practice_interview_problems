#include "../templates/template.h"





int main(int argc, char const *argv[])
{

    vector<string> sa{"bob", "sue", "tom"};
    stringstream ss;
    int i = 0;
    for_each(all(sa), [&](auto s)
    {
        if (i != 0)
        {
            // tail insertion
            ss << ",";
        }
        // tail insertion
        ss << s;
        ++i;
     });

    cout<<ss.str()<<endl;
    return 0;
}
