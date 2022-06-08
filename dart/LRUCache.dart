import 'dart:collection';
import 'dart:core';

import 'dart:io';

class MyTup extends LinkedListEntry<MyTup>
{
  int key, value;

  MyTup(this.key, this.value);

  @override
  String toString() {
    return "$key $value";
  }
}

class LRUCache
{
  HashMap<int, MyTup> map;

  // least recent used =====> most recently used
  LinkedList<MyTup> l;
  int cap;

  void p(Object m) => print(m);

  LRUCache(int capacity)
  {
    cap = capacity;
    map = new HashMap<int, MyTup>();
    l = new LinkedList<MyTup>();
  }

  // tail insertion
  void MoveToMostRecentlyUsed(int key)
  {
    l.remove(map[key]);
    l.add(map[key]);
  }

  int get(int key)
  {
    if (!map.containsKey(key))
    {
      return -1;
    }

    // remove and append to tail
    MoveToMostRecentlyUsed(key);

    stdout.write('linked list:');
    printll();

    return map[key].value;
  }

  void put(int key, int val)
  {
    if (map.containsKey(key))
    {
      map[key].value = val;
      MoveToMostRecentlyUsed(key);
    }
    else
    {
      // p("-----");
      if (map.length >= cap)
      {
        int k = l.first.key;
        //printll();
        map.remove(k);
        l.remove(l.first);
        // p("---");
        //printll();
      }
      map[key] = new MyTup(key, val);
      l.add(map[key]);
      //p("finally:");
      // printll();
    }

    printll();
    p('');
  }

  void printll()
  {
    if (l.first == null) return;
    MyTup tmp = l.first;
    while (tmp != null)
    {
      stdout.write(" (${tmp.key},${tmp.value}) ");
      tmp = tmp.next;
    }
    // print('');
  }
}

void main(List<String> args)
{
  LRUCache lRUCache = new LRUCache(2);
  lRUCache.put(1, 1); // cache is {1=1}
  lRUCache.put(2, 2); // cache is {1=1, 2=2}
  print(lRUCache.get(1));    // return 1
  lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
  print(lRUCache.get(2));    // returns -1 (not found)
  lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
  print(lRUCache.get(1));    // return -1 (not found)
  print(lRUCache.get(3));    // return 3
  print(lRUCache.get(4));    // return 4
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */
