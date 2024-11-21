
#include "../templates/template.h"

// this took me so many hours to do in C++
// very difficult and a lot to keep track of on paper
// here it is. Should be easily portable to C

template<class T=int>
class MyLinkedList
{
private:
    struct Node
    {
        T val;
        Node* next;
        Node(T i) : val(i)
        {}
    };

    Node* head, *tail;
    int len = 0;

    // will have a default value of whatever type it is given
    T dummy_val;

public:
    /** Initialize your data structure here. */
    MyLinkedList(){}
    ~MyLinkedList(){destroyList(head);}

    // keep track of list size for debugging purposes
    int size() { return len; }

    // recursively cleans up list
    void destroyList(Node* h)
    {
        if (!h) return;
        destroyList(h->next);
        delete h;
    }

    // for debugging purposes
    void printll()
    {
        auto tmp = head;
        while (tmp)
        {
            cout<<tmp->val<<", ";
            tmp = tmp->next;
        }
        nl;
    }

    // for debugging purposes
    T headVal() { return head->val; }

    // for debugging purposes
    T tailVal() { return tail->val; }

    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    T get(int index)
    {
        int cnt = 0;
        auto tmp = head;

        // traverse thru list just like you would for an array
        while (tmp)
        {
            if (cnt == index)
            {
                return tmp->val;
            }
            tmp=tmp->next;
            ++cnt;
        }

        // index >= size of list or index < 0, so return -1
        return dummy_val;
    }

    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(T val)
    {
        // empty list check
        if (len == 0)
        {
            head = new Node(val);

            // must explicity set next pointers to null in C/C++
            head->next = null;
            tail = head;
            ++len;
            return;
        }

        // head insert
        auto node = new Node(val);
        node->next = head;
        head = node;
        ++len;
    }

    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(T val)
    {
        // empty list check
        if (len == 0)
        {
            head = new Node(val);

            // must explicity set next pointers to null in C/C++
            head->next = null;
            tail = head;
            ++len;
            return;
        }

        // tail insert
        auto node = new Node(val);

        // must explicity set next pointers to null in C/C++
        node->next = null;
        tail->next = node;
        tail = node;
        ++len;
    }

    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, T val)
    {
        if (index > len) return;

        // empty list check
        if (len == 0)
        {
            head = new Node(val);

            // must explicity set next pointers to null in C/C++
            head->next = null;
            tail = head;
            ++len;
            return;
        }

        auto node = new Node(val);

        // tail insertion
        if (index == len)
        {
            tail->next = node;

            // must explicity set next pointers to null in C/C++
            node->next = null;
            tail = node;
            ++len;
            return;
        }

        // head insertion
        if (index == 0)
        {
            node->next = head;
            head = node;
            ++len;
            return;
        }

        auto tmp = head;
        int i;
        for (i = 0;i < index-1;++i)
            tmp = tmp->next;
        auto next = tmp->next;
        tmp->next = node;
        node->next = next;
        ++len;
    }

    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index)
    {
        if (index >= len) return;

        // empty list check
        if (index == 0)
        {
            auto tmp = head;
            head = head->next;
            delete tmp;
            --len;
            return;
        }

        // tail deletion
        if (index == len-1)
        {
            cout<<"tail val is "<<tail->val<<endl;
            auto tmp = head;
            while (tmp->next != tail)
            {
                cout<<tmp->val<<' ';
                tmp = tmp->next;
            }
            nl;
            // cout<<tmp->next->val<<endl;
            auto toDel = tail;
            tail = tmp;
            tail->next = null;
            delete toDel;
            --len;
            return;
        }

        auto tmp = head;
        int i;
        for (i = 0;i < index-1;++i)
            tmp = tmp->next;
        auto toDel = tmp->next;
        auto next = tmp->next->next;
        tmp->next = next;
        delete toDel;
        --len;
    }
};

/*
 ["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
[[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]

["MyLinkedList","addAtHead","addAtIndex","get","addAtHead","get","addAtHead","get","get","addAtIndex","addAtTail","addAtHead"]
[   [],            [0],         [1,1],    [2],      [4],    [2],     [4],     [2],   [3],  [1,6],        [1],         [0]]
 */
int main(int argc, char const *argv[])
{
    MyLinkedList<char> l;
    #pragma region
    // l->addAtHead(2);
    // l->printll();
    // l->deleteAtIndex(1);
    // l->addAtHead(2);
    // l->addAtHead(7);

    // l->addAtHead(3);
    // l->addAtHead(2);
    // l->addAtHead(5);
    // l->addAtTail(5);
    // deb(l->get(5));
    // l->deleteAtIndex(6);
    // l->deleteAtIndex(4);
    // deb(l->headVal());
    // deb(l->tailVal());
    // deb(l->size());
    // l->printll();
    #pragma endregion

    #pragma region
    // l.addAtHead(0);
    // l.addAtIndex(1,1);
    // // deb(l->get(2));
    // l.addAtHead(4);
    // // deb(l->get(2));
    // l.addAtHead(4);
    // // deb(l->get(2));
    // // deb(l->get(3));
    // l.addAtIndex(1,6);
    // l.addAtTail(1);
    // l.addAtHead(0);
    // deb(l.headVal());
    // deb(l.tailVal());
    // deb(l.size());
    // deb(l.get(545454));
    // l.printll();
    #pragma endregion

    l.addAtHead('a');
    l.printll();
    l.addAtIndex(1,'b');
    l.printll();
    // deb(l->get(2));
    l.addAtHead('c');
    l.printll();
    // deb(l->get(2));
    l.addAtHead('d');
    l.printll();
    // deb(l->get(2));
    // deb(l->get(3));
    l.addAtIndex(1,'e');
    l.printll();
    l.addAtTail('f');
    l.printll();
    l.addAtHead('g');
    // deb(l.headVal());
    // deb(l.tailVal());
    // deb(l.size());
    // deb(l.get(545454));
    l.printll();

    return 0;
}
