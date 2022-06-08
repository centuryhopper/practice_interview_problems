using namespace std;
#define gc getchar_unlocked
#define fo(i,n) for(i=0;i<n;i++)
#define FOR(i,k,n)




class MyCircularQueue
{
private:
    int* ar;
    int front, rear;
    int cap;

public:
    MyCircularQueue(int k)
    {
        ar = new int[k];
        // memset(ar, -1, sizeof(ar)*k);
        front = rear = -1;
        cap = k;
    }
    ~MyCircularQueue()
    {
        delete[] ar;
    }

    bool enQueue(int value)
    {
        if (isFull())
        {
            return false;
        }
        if (isEmpty())
            front++;
        rear++;
        rear %= cap;
        ar[rear] = value;
        return true;
    }

    bool deQueue()
    {
        if (isEmpty()) return false;
        // the queue is empty again
        if (front == rear)
            front = rear = -1;
        else
            front = (front + 1) % cap;

        return true;
    }

    int Front()
    {
        return isEmpty() ? -1 : ar[front];
    }

    int Rear()
    {
        // for (int i = 0;i < cap;++i)
        //     cout << ar[i] << " ";
        // cout << "\n";
        return isEmpty() ? -1 : ar[rear];
    }

    bool isEmpty()
    {
        return front == -1;
    }

    bool isFull()
    {
        return (rear+1)%cap == front;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */