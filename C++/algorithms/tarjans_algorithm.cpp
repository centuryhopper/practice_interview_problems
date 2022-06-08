#include "../templates/template.h"

class Solution
{
private:
    vvi adjLst;
    vvi ret;
    vector<int> lowTime, dfsNumber;
    int time = 0;

    void buildAdjacencyLst(const vvi& cs)
    {
        adjLst.resize(cs.size());
        for (vector<int> c : cs)
        {
            this->adjLst[c[0]].eb(c[1]);
            this->adjLst[c[1]].eb(c[0]);
        }
    }

    // base case parentNode is -1 to kick off the dfs recursive calls
    void dfs(vector<bool>& visited, int curNode, int parentNode)
    {
        visited[curNode] = true;
        dfsNumber[curNode] = lowTime[curNode] = time++;

        // dfs thru each adjacent node
        for (int neighbor : adjLst[curNode])
        {
            // we don't want to dfs back to our parent
            // otherwise, we would have infinite recursion (stack overflow)
            if (neighbor == parentNode) continue;

            if (!visited[neighbor])
            {
                dfs(visited, neighbor, curNode);
                // back propagate
                lowTime[curNode] = min(lowTime[curNode], lowTime[neighbor]);
                if (dfsNumber[curNode] < lowTime[neighbor])
                {
                    vector<int> tmp{curNode, neighbor};
                    ret.eb(tmp);
                }
            }
            // found a back edge
            else
            {
                lowTime[curNode] = min(lowTime[curNode], dfsNumber[neighbor]);
            }
        }

    }

public:
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections)
    {
        buildAdjacencyLst(connections);
        // for (auto l : adjLst) { p(l);nl; }
        vector<bool> visited(n, false);
        // ret.resize(n);
        lowTime.resize(n); dfsNumber.resize(n);
        dfs(visited,0,-1);


        return ret;

    }
};




        // // holds the number of vertex in the order it's traversed
        // vector<int> dfsnum(n,-1);
        // // holds the number of vertex with minimum vertex number which can be reached from it (back edge)
        // vector<int> low(n,-1);
        // // holds the flag for vertex in stack or not
