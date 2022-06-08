#include "../templates/template.h"

class DisjointSet
{
    // decides which value becomes the parent
    // (i.e. higher ranked values will become the parent of lower ranked values)
    int *rank;
    // an array to track the current parent of the ith index
    int *parent;
    // number of values we have (i.e. 0 to n-1)
    int n;

public:
    DisjointSet(int n) : rank(new int[n]), parent(new int[n]), n(n)
    {
        cout<<"n is "<<this->n<<endl;
        makeSet();
        // printRanks();
        // printParents();
    }
    ~DisjointSet()
    {
        delete[] rank;
        delete[] parent;
    }

    void printRanks()
    {
        for (int i = 0; i < n;++i)
            cout<<'('<<i<<','<<rank[i]<<')'<<' ';
        nl;
    }

    void printParents()
    {
        for (int i = 0; i < n;++i)
            cout<<'('<<i<<','<<parent[i]<<')'<<' ';
        nl;
    }

    // initialize all values (resets all previous data, so be careful when calling this method!)
    void makeSet()
    {
        for (int i = 0; i < this->n; ++i)
            parent[i] = i;
        // initializes the entire rank array to all 0s
        memset(rank,0,sizeof(rank)*n);
    }
    int find(int x)
    {
        // error check
        if (x < 0 || x >= this->n)
            return -1;

        // find representative of set that x belongs to
        if (parent[x] == x)
            return x;

        // path compression
        parent[x] = find(parent[x]);

        return parent[x];
    }
    void Union(int x, int y)
    {
        // find representatives of the sets x and y belongs to
        int xRepresentative = find(x);
        int yRepresentative = find(y);

        if (xRepresentative == -1)
        {
            cout<<"can't union "<<xRepresentative<<" because it doesn't exist";
            return;
        }
        if (yRepresentative == -1)
        {
            cout<<"can't union "<<yRepresentative<<" because it doesn't exist";
            return;
        }

        // don't do anything if x and y already belong to the same set
        if (xRepresentative == yRepresentative)
        {
            cout<<x<<" and "<<y<<" are already in the same set."<<endl;
            return;
        }
        if (rank[xRepresentative] < rank[yRepresentative])
        {
            parent[xRepresentative] = yRepresentative;
        }
        else if (rank[yRepresentative] < rank[xRepresentative])
        {
            parent[yRepresentative] = xRepresentative;
        }
        // here it doesn't matter who is the parent, so we'll
        // just let x representative be the parent
        else if (rank[xRepresentative] == rank[yRepresentative])
        {
            parent[yRepresentative] = xRepresentative;
            rank[xRepresentative] += 1;
        }

        // could potentially print ranks and parents here as well to help with visualization
    }
};

int main(int argc, const char **argv)
{
    int n = 7;
    DisjointSet ds(n);
    ds.Union(0,1);
    ds.Union(1,2);
    ds.Union(3,4);
    ds.Union(5,6);
    ds.Union(4,5);
    ds.Union(2,6);
    for (int i = 0; i < n; ++i)
    {
        printf("%d belongs to set %d\n",i,ds.find(i));
    }

    // layout the parents and ranks of each value
    ds.printRanks();
    ds.printParents();

    return 0;
}
