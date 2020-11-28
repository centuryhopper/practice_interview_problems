using System;
using System.Collections.Generic;

namespace practice_problems
{
    public class RandomizedSet
    {
        // key: the number to be put in the set.
        // value: the index of that number in the list
        Dictionary<int, int> d;
        List<int> l;
        Random r;

        /** Initialize your data structure here. */
        public RandomizedSet()
        {
            l = new List<int>();
            d = new Dictionary<int, int>();
            r = new Random();
        }

        /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
        public bool Insert(int val)
        {
            if (d.TryAdd(val, l.Count))
            {
                l.Add(val);
                return true;
            }
            return false;
        }

        /** Removes a value from the set. Returns true if the set contained the specified element. */
        public bool Remove(int val)
        {
            if (!d.ContainsKey(val)) { return false; }

            // get value from 'val'
            int listInd = d[val];

            // get last element in the list
            int tail = l[l.Count - 1];

            // find last element in the map and change its pos
            d[tail] = listInd;

            l[listInd] = tail;

            // This action is O (1) only because we're removing from the tail
            // if we were removing from the head, then the runtime is O(n),
            // where n is the length of the list
            l.RemoveAt(l.Count - 1);

            return d.Remove(val);
        }

        /** Get a random element from the set. */
        public int GetRandom()
        {
            int randInd = r.Next(l.Count);
            return l[randInd];
        }
    }

    /**
     * Your RandomizedSet object will be instantiated and called as such:
     * RandomizedSet obj = new RandomizedSet();
     * bool param_1 = obj.Insert(val);
     * bool param_2 = obj.Remove(val);
     * int param_3 = obj.GetRandom();
     */
}