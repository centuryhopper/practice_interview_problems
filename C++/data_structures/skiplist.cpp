#include "../templates/template.h"

// minimum level is 0
class Skiplist
{
private:
    struct Node
    {
    private:
        int level;
        int val;
        vector<Node *> refs;

    public:
        // any new node upon creation should point to null
        Node(int level, int val) : level(level), val(val), refs(level, null) {}
        int levels() { return this->refs.size(); }
        int value() { return this->val; }

        void addHeight()
        {
            this->refs.push_back(null);
        }

        // sets the next pointer at the ith level to specified reference
        void setNext(int i, Node *node)
        {
            if (i < 0 || i > refs.size())
            {
                cout << "level out of bounds" << endl;
                return;
            }
            this->refs[i] = node;
        }

        Node *next(int i)
        {
            if (i < 0 || i > refs.size())
            {
                cout << "level out of bounds" << endl;
                return null;
            }
            return this->refs[i];
        }
    };

    // no other node should be taller than head height
    Node *head;
    int listSize = 0;

    // generate a random height for a new node
    int getRandomHeight()
    {
        int val = 1;
        while (rand() % 2 == 1)
            ++val;
        return val;
    }

    // all existing nodes are guaranteed to have a reference at level 0
    void destroy(Node *h)
    {
        if (!h)
            return;
        destroy(h->next(0));
        delete h;
    }

public:
    // start at the top and go down if needed
    Skiplist() : head(new Node(1, INT_MIN))
    {
    }

    ~Skiplist()
    {
        printf("skiplist destroyed\n");
        destroy(this->head);
    }

    // return the number of elements in the skiplist
    int size() { return this->listSize; }

    // debugging
    void print()
    {
        cout << "height of skiplist: " << head->levels() << endl;
        auto tmp = head;
        int ht = head->levels() - 1;
        while (ht >= 0)
        {
            while (tmp)
            {
                cout << tmp->value() << ", ";
                tmp = tmp->next(ht);
            }
            // set tmp back to head for the next level below
            tmp = head;
            cout << endl;
            --ht;
        }
    }

    void printFirstLevel()
    {
        cout << "height of skiplist: " << head->levels() << endl;
        auto tmp = head;
        while (tmp)
        {
            cout << tmp->value() << ", ";
            tmp = tmp->next(0);
        }
        cout << endl;
    }

    bool search(int target)
    {
        auto tmp = head;
        int htIdx = tmp->levels() - 1;
        while (htIdx >= 0)
        {
            // move down if next pointer is null or the value at next pointer is greater than target
            if (!tmp->next(htIdx) || tmp->next(htIdx)->value() > target)
            {
                htIdx--;
            }
            // move right if value is less than target
            else if (tmp->next(htIdx)->value() < target)
            {
                tmp = tmp->next(htIdx);
            }
            else
            {
                return true;
            }
        }

        // didn't find it, so return false
        return false;
    }

    // duplicates will be inserted before instead of after
    void add(int num)
    {
        int newNodeHt = getRandomHeight();
        auto node = new Node(newNodeHt, num);
        while (head->levels() < newNodeHt)
            head->addHeight();

        auto tmp = head;

        // traverse the height of our new node
        int htIdx = tmp->levels() - 1;
        while (htIdx >= 0)
        {
            // move down if next pointer is null or the value at next pointer is greater than or equal to target
            if (!tmp->next(htIdx) || tmp->next(htIdx)->value() >= num)
            {
                // can't start linking until we're at most as tall as the height of the new node
                if (htIdx < newNodeHt)
                {
                    // we know for sure that this node's next must point to the new node
                    // because we're traversing from the height of our new node
                    Node *t = tmp->next(htIdx);
                    tmp->setNext(htIdx, node);
                    node->setNext(htIdx, t);
                }

                // drop down a level
                htIdx--;
            }

            // move right if value is less than target
            else if (tmp->next(htIdx)->value() < num)
            {
                tmp = tmp->next(htIdx);
            }
        }

        ++listSize;
    }

    bool erase(int num)
    {
        if (listSize == 0)
            return false;

        auto tmp = head;
        int htIdx = tmp->levels() - 1;

        Node *target = null;

        while (htIdx >= 0)
        {
            // move down if next pointer is null or the value at next pointer is greater than target
            if (!tmp->next(htIdx) || tmp->next(htIdx)->value() > num)
            {
                htIdx--;
            }
            // move right if value is less than
            else if (tmp->next(htIdx)->value() < num)
            {
                tmp = tmp->next(htIdx);
            }
            // found value to delete so unlink its reference at level 'htIdx'
            else
            {
                target = tmp->next(htIdx);
                tmp->setNext(htIdx, target->next(htIdx));
                --htIdx;
            }
        }

        if (target)
        {
            --listSize;
            delete target;
            return true;
        }

        return false;
    }
};

/*
["Skiplist","add","add","add","search","add","search","erase","erase","search"]
[   [],      [1],  [2],  [3],    [0],   [4],    [1],    [0],    [1],    [1]]
 */

int main(int argc, char const *argv[])
{
    std::cout << std::boolalpha << std::endl;
    srand(time(NULL));

    Skiplist s;

    clock_t t = clock();
    for (int i = 0; i < 100; ++i)
        s.add((rand() % 101) + 1);

    // s.add(1);
    // s.add(2);
    // s.add(3);
    // std::cout << s.search(0) << std::endl;
    // s.add(4);
    // s.print();
    // nl;
    // std::cout << s.search(1) << std::endl;
    // std::cout << s.erase(0) << std::endl;
    // std::cout << s.erase(1) << std::endl;
    std::cout << s.search(99) << std::endl;
    // std::cout << s.size() << std::endl;
    // std::cout << s.erase(6) << std::endl;
    s.printFirstLevel();
    t = clock() - t;

    printf("It took me %d clicks (%f seconds).\n", t, ((float)t) / CLOCKS_PER_SEC);

    return 0;
}
