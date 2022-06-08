namespace practice_problems
{
    public class Pow
    {
        // 2^5 = 2 * 2 * 2 * 2 * 2
        // 2^-5 = 1 / (2 * 2 * 2 * 2 * 2)
        public double MyPowLogNTime(double x, int n)
        {
            // helper method
            double MyPowHelper(double x, int n)
            {
                if (n == 0) return 1;
                if (n == 1) return x;
                bool isOdd = n % 2 == 1;
                return isOdd ? MyPowHelper(x * x, n / 2) * x : MyPowHelper(x * x, n / 2);
            }

            if (x == 1 || x == 0) return x;
            if (x == -1)
            {
                return n % 2 == 0 ? 1 : -1;
            }
            if (n == int.MinValue) return 0;
            return n > 0 ? MyPowHelper(x, n) : (1 / MyPowHelper(x, -n));
        }

        public double MyPow(double x, int n)
        {
            double PowRunner(double x, int n)
            {
                if (n == 0) return 1;
                if (n == 1) return x;

                return x * PowRunner(x, n - 1);
            }

            if (n >= 0) { return PowRunner(x, n); }

            return 1 / PowRunner(x, -n);
        }

        public double MyPowIterative(double x, int n)
        {
            if (n == 0) return 1;

            bool isNeg = false;
            if (n < 0)
            {
                isNeg = true;
            }

            n = isNeg ? (n * -1) : n;
            double multRes = 1;
            for (int i = 0; i < n; ++i)
            {
                multRes *= x;
            }

            return isNeg ? 1 / multRes : multRes;
        }
    }
}