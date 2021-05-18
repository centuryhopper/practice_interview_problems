class Solution {
public:
    int countPrimes(int n)
    {
        if (n <= 2)
            return 0;

        bool primes[n];
        for(int i = 0;i<n;++i) primes[i] = true;

        for (int i = 2; i*i < n; i += 1)
        {
            if (primes[i])
            {
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
};