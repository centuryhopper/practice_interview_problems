#include "../templates/template.h"

class MyHashSet
{

private:
    int ar[100001];

    int hashFunc(int key)
    {
        return key % 100001;
    }

public:
    /** Initialize your data structure here. */
    MyHashSet()
    {
        memset(ar,-1,sizeof(ar));
    }

    void add(int key)
    {
        ar[hashFunc(key)] = key;
    }

    void remove(int key)
    {
        ar[hashFunc(key)] = -1;
    }

    /** Returns true if this set contains the specified element */
    bool contains(int key)
    {
        return ar[hashFunc(key)] == key;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */



