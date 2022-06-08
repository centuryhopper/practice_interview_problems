#include "../templates/template.h"


class MyHashTable
{
private:
    vector<pair<int,int>> ar;

public:
    /** Initialize your data structure here. */
    MyHashTable()
    {
        ar.resize(100001);
        for (int i = 0; i < 100001; ++i)
        {
            ar[i] = {-1,-1};
        }
    }

    int hashFunc(int key)
    {
        return key % 100001;
    }

    /** value will always be non-negative. */
    void put(int key, int value)
    {
        int idx = hashFunc(key);
        ar[idx] = {key, value};
    }

    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    int get(int key)
    {
        int idx = hashFunc(key);
        return ar[idx].first == -1 ? -1 : ar[idx].second;
    }

    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    void remove(int key)
    {
        int idx = hashFunc(key);
        ar[idx] = {-1,-1};
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */