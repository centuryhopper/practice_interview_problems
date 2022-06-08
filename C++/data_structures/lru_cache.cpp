#include <bits/stdc++.h>

class LRUCache
{
private:
    std::unordered_map<int, std::list<std::pair<int, int>>::iterator> m;
    // doubly linked list
    std::list<std::pair<int, int>> l;
    int cap;

    // tail insertion
    void MoveToMostRecentlyUsed(int key)
    {
        // where, which list, and what value
        l.splice(l.end(), l, m[key]);
    }

public:
    LRUCache(int capacity)
    {
        cap = capacity;
    }
    ~LRUCache() {}

    int get(int key)
    {
        // couldn't find the key
        if (m.find(key) == m.end())
        {
            return -1;
        }

        MoveToMostRecentlyUsed(key);

        return m[key]->second;
    }

    void put(int key, int value)
    {
        if (m.find(key) != m.end())
        {
            m[key]->second = value;
            MoveToMostRecentlyUsed(key);
        }
        else
        {
            if (m.size() >= cap)
            {
                m.erase(l.front().first);
                l.pop_front();
            }

            l.push_back({key, value});
            auto tmpIter = l.end();
            // l.end() is pointing at the position
            // right after the last element
            // in the list, so decrement it to access the last element
            tmpIter--;
            m[key] = tmpIter;
        }
    }

    void printll()
    {
        // linked list contents
        for (const auto &node : l)
        {
            std::cout << node.first << ', ' << node.second << "\n";
        }
    }
};

/**
 * LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */