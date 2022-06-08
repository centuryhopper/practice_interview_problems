
namespace practice_problems
{
    public class KthFactorOfN
    {
        // tail recursive method
        // method assumes n >= k
        public int KthFactor(int n, int k) => (n < k) ? -1 : helper(n, k, 1);

        private int helper(int n, int k, int acc)
        {
            // we need to return what acc was right before acc incremented
            // for the last time before k became 0
            // otherwise if we just return acc, edge cases such
            // as n = 7, k = 2, and acc = 1, initially, will fail
            if (k == 0) return acc - 1;
            if (acc > n) return -1;

            // only decrement k if n % acc is 0
            return helper(n, (n % acc == 0) ? k - 1 : k, acc + 1);
        }
    }
}