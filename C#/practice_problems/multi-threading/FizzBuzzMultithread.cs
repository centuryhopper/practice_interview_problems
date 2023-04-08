using System.Threading;

/*
structure:

while (true)
{
    // lock the shared resource
    mutex.WaitOne();

    // avoid going out of bounds
    if (cnt > n)
    {
        mutex.ReleaseMutex();
        return;
    }

    if (condition is met)
    {
        *Invoke the print function*
        increment count
    }

    // at this point release the mutex no matter what
    mutex.ReleaseMutex();
}

*/

public class FizzBuzz
{
    private int n;
    private Mutex mutex = new Mutex();
    private int cnt = 1;

    public FizzBuzz(int n)
    {
        this.n = n;
    }

    // printFizz() outputs "fizz".
    public void Fizz(Action printFizz)
    {
        while (true)
        {
            mutex.WaitOne();
            if (cnt > n)
            {
                mutex.ReleaseMutex();
                return;
            }
            if (cnt % 3 == 0 && cnt % 5 != 0)
            {
                printFizz.Invoke();
                cnt++;
            }
            mutex.ReleaseMutex();
        }
    }


    // printBuzzz() outputs "buzz".
    public void Buzz(Action printBuzz)
    {
        while (true)
        {
            mutex.WaitOne();
            if (cnt > n)
            {
                mutex.ReleaseMutex();
                return;
            }
            if (cnt % 3 != 0 && cnt % 5 == 0)
            {
                printBuzz.Invoke();
                cnt++;
            }
            mutex.ReleaseMutex();
        }
    }

    // printFizzBuzz() outputs "fizzbuzz".
    public void Fizzbuzz(Action printFizzBuzz)
    {
        while (true)
        {
            mutex.WaitOne();
            if (cnt > n)
            {
                mutex.ReleaseMutex();
                return;
            }
            if (cnt % 3 == 0 && cnt % 5 == 0)
            {
                printFizzBuzz.Invoke();
                cnt++;
            }
            mutex.ReleaseMutex();
        }
    }

    // printNumber(x) outputs "x", where x is an integer.
    public void Number(Action<int> printNumber)
    {
        while (true)
        {
            mutex.WaitOne();
            if (cnt > n)
            {
                mutex.ReleaseMutex();
                return;
            }
            if (cnt % 3 != 0 && cnt % 5 != 0)
            {
                printNumber.Invoke(cnt);
                cnt++;
            }
            mutex.ReleaseMutex();
        }
    }
}
