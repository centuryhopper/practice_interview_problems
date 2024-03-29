package multithreading;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class LivelockExample
{
    private Lock lock1 = new ReentrantLock(true);
    private Lock lock2 = new ReentrantLock(true);

    public static void main(String[] args)
    {
        LivelockExample livelock = new LivelockExample();
        new Thread(() ->
        {
            try
            {
                livelock.operation1();
            } catch (InterruptedException e)
            {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }, "T1").start();
        new Thread(() ->
        {
            try
            {
                livelock.operation2();
            } catch (InterruptedException e)
            {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
        }, "T2").start();
    }

    private void print(Object m)
    {
        System.out.println(m);
    }

    public void operation1() throws InterruptedException
    {
        while (true)
        {
            lock1.tryLock();
            print("lock1 acquired, trying to acquire lock2.");
            Thread.sleep(50);

            if (lock2.tryLock())
            {
                print("lock2 acquired.");
            } else
            {
                print("cannot acquire lock2, releasing lock1.");
                lock1.unlock();
                continue;
            }

            print("executing first operation.");
            break;
        }
        lock2.unlock();
        lock1.unlock();
    }

    public void operation2() throws InterruptedException
    {
        while (true)
        {
            lock2.tryLock();
            print("lock2 acquired, trying to acquire lock1.");
            Thread.sleep(50);

            if (lock1.tryLock())
            {
                print("lock1 acquired.");
            } else
            {
                print("cannot acquire lock1, releasing lock2.");
                lock2.unlock();
                continue;
            }

            print("executing second operation.");
            break;
        }
        lock1.unlock();
        lock2.unlock();
    }
}
