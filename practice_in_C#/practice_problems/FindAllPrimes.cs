using System;

namespace practice_problems
{
    public class FindAllPrimes
    {
        // sieve of eratosthenes algorithm
        public int CountPrimes(int n)
        {
            if (n <= 2)
                return 0;

            bool[] primes = new bool[n];
            Array.Fill(primes, true);

            int ub = (int)Math.Sqrt(n);
            for (int i = 2; i <= ub; i += 1)
            {
                if (primes[i])
                {
                    // start at the square of i and sieve
                    // all multiples of i (optimized)
                    for (int j = i * i; j < n; j += i)
                        primes[j] = false;
                }
            }

            // 1 because 2 is prime
            int cnt = 1;
            for (int i = 3; i < n; i += 2)
                cnt = primes[i] ? cnt + 1 : cnt;

            return cnt;
        }
    }
}