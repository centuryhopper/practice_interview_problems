#include "../templates/template.h"
template<typename A> void print_queue(A& pq)
{
	while (!pq.empty())
		{
			cout << pq.top() << endl;
			pq.pop();
		}
}

// time: O(n) in the worst case that we traverse all the buildings
// space: O(l) where l is the number of ladders for the minheap

class Solution
{
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders)
    {
        ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
        int n = heights.size();

        // maintain largest jumps keep the size of the minheap to be the size of the number of ladders
        priority_queue<int, vector<int>, greater<int>> h;

        // preprocess what's ahead and calculate when to use ladder and when to use bricks
        for (int i = 1;i < n;++i)
        {
            int diff = heights[i] - heights[i-1];
            if (diff > 0)
            {
                if (h.size() < ladders)
                {
                    h.push(diff);
                }
                else
                {
                    int brickHeight = diff;

                    // store the largest heights in min heap
                    // get and remove the top element if we find a height that's larger and use bricks on the removed top element
                    if (h.size() > 0 && diff > h.top())
                    {
                        brickHeight = h.top();
                        h.pop();
                        h.push(diff);
                    }
                    if (bricks - brickHeight >= 0)
                    {
                        bricks -= brickHeight;
                    }

                    // can't be here and any further so return the previous allowed spot to be on
                    else
                    {
                        return i - 1;
                    }
                }
            }
        }


        // we made it to the end here
        return heights.size() - 1;
    }
};