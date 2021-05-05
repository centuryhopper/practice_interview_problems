#include "../templates/template.h"


int main(int argc, char const *argv[])
{
    vector<string> lst{"A", "B","C","D","E"};
    // reverse(all(lst));

    stringstream ss(lst[lst.size()-1]);

    for (auto it = lst.rbegin()+1; it != lst.rend();++it)
    {
        ss << " " << *it;
    }

    cout << ss.str() << endl;

    // string s;
    // stringstream st;
    // vector<string> tmp;
    // while (getline(st, ss.str(),','))
    // {
    //     tmp.pb(s);
    // }

    // p(tmp);


    return 0;
}

