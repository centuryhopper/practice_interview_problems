using System;
using System.Threading;

public class Foo
{
    // Set will signal the next waitOne to proceed
    // AutoResetEvent e, e2;
    // Mutex m, m2;
    Semaphore s1, s2, s3;
    public Foo()
    {
        // e = new AutoResetEvent(false);
        // e2 = new AutoResetEvent(false);
        // m = new Mutex();
        // m2 = new Mutex();

        // new Semaphore(x,y) where 0 <= x <= y
        // important: you don't have to call waitone() before you call release() for
        // any semaphore
        s1 = new Semaphore(1,1);
        s2 = new Semaphore(0,1);
        s3 = new Semaphore(0,1);
    }

    ~Foo()
    {
        // clean up
        s1.Dispose();
        s2.Dispose();
        s3.Dispose();
    }

    public void First(Action printFirst)
    {

        s1.WaitOne();
        // this method has no waitOne() from the autoresetevent, so it will be called first
        // m.WaitOne();
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();

        // signal the second() method
        // e.Set();
        // m.ReleaseMutex();

        // calls the second()
        s2.Release();
    }

    public void Second(Action printSecond)
    {

        s2.WaitOne();
        // e.WaitOne();
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();

        // signal the third() method
        // e2.Set();

        // calls the third()
        s3.Release();
    }

    public void Third(Action printThird)
    {
        s3.WaitOne();
        // e2.WaitOne();
        // printThird() outputs "third". Do not change or remove this line.
        printThird();

        s1.Release();
    }
}