#include <bits/stdc++.h>


using namespace std;

class Solution
{
    /*
    0, 0001   0001
    1, 0010   0011 (1 after visiting 0)
    2, 0100   0111 (2 after visiting 0,1)
    3, 1000   1111 (3 after visiting 0,1,2)


    */
public:
    int shortestPathLength(vector<vector<int>>& graph)
    {
        int n = graph.size();
        if (n < 2) return 0;
        // get final bit state
        // should be 111...n times
        // final bit state
        const int FINAL_STATE = (1 << n) - 1;
        // visited states
        // current node, current state
        set<pair<int,int>> m;

        queue<pair<int,int>> q;

        // add all nodes because we can start anywhere
        for (int i = 0; i < n; i++)
            q.push({i,1 << i});

        int minPath = 0;

        // bfs
        while (!q.empty())
        {
            int size = q.size();
            minPath++;
            for (int i = 0; i < size; ++i)
            {
                auto cur = q.front(); q.pop();
                int visitedNodeState = cur.second;
                for (auto neighbor : graph[cur.first])
                {
                    int newState = (1 << neighbor) | visitedNodeState;
                    // if state has been visited, skip it
                    if (m.find({neighbor, newState}) != m.end())
                    {
                        continue;
                    }

                    q.push({neighbor, newState});
                    // immediately mark as visited to avoid it being seen again in another iteration
                    m.insert({neighbor, newState});
                    if (newState == FINAL_STATE)
                        return minPath;
                }
            }
        }

        // something went wrong
        return -1;

    }
};