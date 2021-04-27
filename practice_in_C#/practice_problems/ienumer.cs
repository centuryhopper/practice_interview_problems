using System;
using System.Collections.Generic;

namespace CollatzCSharp
{
    class ienumer
    {
        public static IEnumerable<(uint count, uint value)> Collatz(uint seed)
        {
            uint count = 1;

            yield return (count, seed);

            while (seed > 1)
            {
                if (seed % 2 == 0)
                    seed /= 2;
                else
                    seed = 3 * seed + 1;

                yield return (++count, seed);
            }
        }

        static void Main()
        {
            foreach (var (count, value) in Collatz(1000))
            {
                Console.WriteLine($"{count}: {value}.");
            }
        }
    }
}