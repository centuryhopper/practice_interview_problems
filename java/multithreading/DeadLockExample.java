package multithreading;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class DeadLockExample
{
    private Lock lock1 = new ReentrantLock(true);
    private Lock lock2 = new ReentrantLock(true);

    public static void main(String[] args)
    {
        DeadLockExample deadlock = new DeadLockExample();
        new Thread(() ->
        {
            try
            {
                deadlock.operation1();
            } catch (InterruptedException e)
            {
                e.printStackTrace();
            }
        }, "T1").start();
        new Thread(() ->
        {
            try
            {
                deadlock.operation2();
            } catch (InterruptedException e)
            {
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
        lock1.lock();
        print("lock1 acquired, waiting to acquire lock2.");
        Thread.sleep(50);

        lock2.lock();
        print("lock2 acquired");

        print("executing first operation.");

        lock2.unlock();
        lock1.unlock();
    }

    public void operation2() throws InterruptedException
    {
        lock2.lock();
        print("lock2 acquired, waiting to acquire lock1.");
        Thread.sleep(50);

        lock1.lock();
        print("lock1 acquired");

        print("executing second operation.");

        lock1.unlock();
        lock2.unlock();
    }

    // helper methods
}
