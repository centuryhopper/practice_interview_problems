#include "../templates/template.h"

template<class T>
struct PowerSetGenerator
{
private:
    void powerSet(const vector<T>& lst, int i, vector<vector<T>>& ret, vector<T>& path)
    {
        // power set of empty set is just a list containing the empty set
        if (i == lst.size())
        {
            // ret.eb(path);
            p(path);
            nl;
            ret.pb(path);
            return;
        }

        vector<int> pathWithCurrentContents(all(path));
        pathWithCurrentContents.eb(lst[i]);

        // at each step, we can take or don't take the current item at index i

        // don't take the current item
        powerSet(lst, i+1, ret, path);

        // take the current item
        powerSet(lst, i+1, ret, pathWithCurrentContents);
    }
public:
    vvi powerSet(const vector<T>& lst)
    {
        // we know what the size of the powerSet will be ahead of time (2^|lst|)
        vector<vector<T>> ret;
        ret.reserve(pow(2, lst.size()));
        vector<T> path;
        // start from the first element
        powerSet(lst, 0, ret, path);

        return ret;
    }
};

int main(int argc, char const *argv[])
{
    vector<int> input{46,83,77,20,73,3,4,54,56,1,32,45};
    // deb(input.size());
    PowerSetGenerator<int> p;
    auto out = p.powerSet(input);
    // for (auto v : out) { p(v);nl; }
    cout<<"length of power set is " << out.size() << endl;

    return 0;
}



