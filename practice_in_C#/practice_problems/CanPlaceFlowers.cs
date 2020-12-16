namespace practice_problems
{
    public class CanPlaceFlowers
    {
        private bool AdjacentsAreEmpty(int[] a, int i) => a[i - 1] == 0 && a[i + 1] == 0;

        public bool _CanPlaceFlowers(int[] a, int n)
        {
            if (n == 0) return true;
            if (a.Length == 1 && a[0] == 0)
            {
                return n == 1;
            }

            int i = 0;

            if (a[i] == 0)
            {
                if (a[i + 1] == 0)
                {
                    // plantable
                    --n;
                    if (n == 0) return true;
                }
            }

            i += 2;

            while (i < a.Length - 1 && n > 0)
            {
                if (a[i] == 0)
                {
                    if (AdjacentsAreEmpty(a, i))
                    {
                        // plantable
                        --n;
                        if (n == 0) return true;
                        i += 2;
                    }
                    else
                    {
                        i += 1;
                    }
                }

                // skip adjacent 1's
                while (i < a.Length && a[i] == 1)
                {
                    ++i;
                }
            }

            if (i == a.Length - 1 && a[i] == 0)
            {
                if (a[i - 1] == 0)
                    --n;
            }

            return n == 0;
        }
    }
}
