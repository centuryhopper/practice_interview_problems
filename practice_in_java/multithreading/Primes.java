package multithreading;

// import interface_package.myinterface;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.*;
import java.util.*;

public class Primes
{
    // initial value of 1 to account for the 2 being only even prime number
    // will keep track of all prime numbers between 1 and 100 million
    private static AtomicInteger cnt = new AtomicInteger(1);

    // initial value of 2 to account for the 2 being only even prime number
    // will keep track of the sum of all prime numbers between 1 and 100 million
    private static AtomicLong sum = new AtomicLong(2L);

    
    private static List<Integer> primeNumbers = Collections.synchronizedList(new ArrayList<Integer>());

    private static void CheckThreadCompletion(Thread[] threads)
    {
        boolean allThreadsAreDone = false;
        while (!allThreadsAreDone)
        {
            for (Thread t : threads)
            {
                if (t.isAlive())
                {
                    allThreadsAreDone = false;
                    break;
                }
                allThreadsAreDone = true;
            }
            // break will take us here
        }
    }

    // Run each thread one at a time
    private static void RunDemThreads(Thread[] sieveThreads, UseSieves[] cPrimes)
    {
        for (int i = 0; i < sieveThreads.length; i++)
        {
            sieveThreads[i] = new Thread(cPrimes[i]);
            sieveThreads[i].start();
            try
            {
                sieveThreads[i].join();
            } catch (Exception e)
            {
                System.out.println("exception caught");
            }
        }
    }

    // This method sets the starting points for each thread
    private static void CreateThreadWorkers(UseSieves[] cPrimes, int upperBound, boolean[] primes, int[] primeNums)
    {
        for (int i = 0; i < cPrimes.length; i++)
        {
            // create 8 calculateprimes objects each with unique start and ends
            cPrimes[i] = new UseSieves(primeNums[i], upperBound, primes);
        }
    }

    private static void TheFunctionThatDoesEverything()
    {
        int numThreads = 8;
        Thread[] sieveThreads = new Thread[numThreads];
        UseSieves[] cPrimes = new UseSieves[numThreads];
        int upperBound = 100000000;
        boolean[] primes = new boolean[upperBound + 1];
        int[] primeNums = new int[]
        { 3, 5, 7, 11, 13, 17, 31, 41 };
        Arrays.fill(primes, true);
        primes[0] = primes[1] = false;

        // create the threads
        CreateThreadWorkers(cPrimes, upperBound, primes, primeNums);

        // run the threads
        RunDemThreads(sieveThreads, cPrimes);

        // let all the threads process then get all the primes afterwards
        CheckThreadCompletion(sieveThreads);

        // write code here to loop thru 10^8 to get all primes

        ExecutorService ex = Executors.newFixedThreadPool(numThreads);

        var lstofStarts = new int[]
        { 0, 12500000, 25000000, 37500000, 50000000, 62500000, 75000000, 87500000, };

        for (var num : lstofStarts)
        {
            ex.execute(new Runnable()
            {
                private void GetFinalizedContents(int start, boolean[] primes)
                {
                    // #8 threads will count all the primes in its segment
                    // for 1e8, the first thread will count from 0 to 12.5 million, exclusive;
                    // #the second thread will count from 12.5 million to 25 million, exclusive;
                    // #and so on and so forth
                    int offset = 12500000;
                    for (int i = start + 1; i < start + offset; i += 2)
                    {
                        if (primes[i])
                        {
                            sum.addAndGet(i);
                            cnt.incrementAndGet();
                            primeNumbers.add(i);
                        }
                    }
                }

                @Override
                public void run()
                {
                    GetFinalizedContents(num, primes);
                }
            });
        }

        // Wait for all threads to finish their work and join up
        ex.shutdown();
        while (!ex.isTerminated())
        {
            Thread.currentThread().setPriority(Thread.MIN_PRIORITY);
            Thread.yield();
        }

        // #region old way of getting all primes
        // ArrayList<Integer> a = new ArrayList<>();
        // a.add(2);
        // Long sum = 2L;
        // for (int i = 3; i < upperBound; i += 2)
        // {
        // if (primes[i])
        // {
        // a.add(i);
        // sum += i;
        // }
        // }

        // int len = a.size();
        // System.out.println("total sum: " + sum);
        // System.out.println("number of primes: " + len);
        // System.out.println("ten largest primes: " + a.subList(len - 10, len));
        // #endregion
    }

    public static void main(String[] args)
    {
        long start = System.currentTimeMillis();
        TheFunctionThatDoesEverything();

        System.out.println(cnt);
        System.out.println(sum);

        Collections.sort(primeNumbers);
        primeNumbers.subList(primeNumbers.size() - 10, primeNumbers.size()).forEach(i -> System.out.print(i + " "));
        System.out.println();
        System.out.println("Total runtime (in milliseconds): " + (System.currentTimeMillis() - start));
    }
}

class UseSieves implements Runnable
{
    private int startInd, endInd;
    private boolean[] primes;

    public UseSieves(int startInd, int endInd, boolean[] primes)
    {
        this.startInd = startInd;
        this.endInd = endInd;
        this.primes = primes;
    }

    public synchronized void SieveEmForGood()
    {
        // caching should increase efficiency rather than repeatedly
        // making the function call
        int res = (int) Math.sqrt(endInd);
        for (int i = startInd; i < res; i += 2)
        {
            if (primes[i])
            {
                for (int j = i * i; j < endInd; j += i)
                {
                    primes[j] = false;
                }
            }
        }
    }

    @Override
    public void run()
    {
        // do sieves here.
        // each thread will sieve the range of numbers in multiples of
        // its starting point
        SieveEmForGood();
    }
}
