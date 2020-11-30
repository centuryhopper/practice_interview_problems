
public class LRUCache
{
    Dictionary<int, LinkedListNode<(int, int)>> d;
    LinkedList<(int, int)> l;
    int cap;

    void p(object m) => Console.WriteLine(m);

    public LRUCache(int capacity)
    {
        cap = capacity;
        d = new Dictionary<int, LinkedListNode<(int, int)>>(capacity);
        l = new LinkedList<(int, int)>();
    }

    // tail insertion
    private void MoveToMostRecentlyUsed(int key)
    {
        l.Remove(d[key]);
        l.AddLast(d[key]);
    }

    public int Get(int key)
    {
        if (!d.ContainsKey(key))
        {
            return -1;
        }
        // remove and append to tail
        MoveToMostRecentlyUsed(key);

        return d[key].Value.Item2;
    }

    public void Put(int key, int val)
    {
        if (d.ContainsKey(key))
        {
            d[key].Value = (key, val);
            MoveToMostRecentlyUsed(key);
        }
        else
        {
            // p("-----");
            if (d.Count >= cap)
            {
                (int k, int v) tup = l.First.Value;
                //printll();
                d.Remove(tup.k);
                l.RemoveFirst();
                // p("---");
                //printll();
            }
            d[key] = new LinkedListNode<(int, int)>((key, val));
            l.AddLast(d[key]);
            //p("finally:");
            // printll();
        }
    }

    void printll()
    {
        if (l.First == null) return;
        LinkedListNode<(int, int)> tmp = l.First;
        while (tmp != null)
        {
            p(string.Format($"{0} {1}", tmp.Value.Item1, tmp.Value.Item2));
            tmp = tmp.Next;
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */