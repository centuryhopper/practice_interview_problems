using System;

namespace practice_problems
{
    public class SumOfTwoIntsUsingBitwiseOperators
    {
        void p(object m) => Console.WriteLine(m);

        /*
            0001
            0010
            ____
            0011  addition

         while (a & b > 0)
            0001
           ^0010
            ____
            0011  xor

            0001
           &0010
            ____
            0000  carries

            a = carries
            b = xor

            a & b:
            0000
            0011
            ____
            0000
        */
        /* recursive method
         public int GetSum(int a, int b)
         {
             if (a == 0) return b;
             int sum = a ^ b, t = (a & b) << 1;
             return GetSum(t, sum);
         }
         */

        // iterative method
        public int GetSum(int a, int b)
        {
            if (a == 0) { return b; }
            if (b == 0) { return a; }

            // we still have carries,
            // keep calculating
            // must be b != 0 instead of b > 0 because b could also be negative at some point
            while (b != 0)
            {
                int carries = a & b;

                a = a ^ b;
                b = carries << 1;
            }

            return a;
        }
    }
}