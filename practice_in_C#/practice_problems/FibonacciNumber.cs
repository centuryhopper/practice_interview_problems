using System;

public class FibonacciNumber
{
    public int Fib(int n)
    {
        // used floats for better performance as high-precision isn't needed
        float goldenRatio = (1+MathF.Sqrt(5))/2;
        return (int)(MathF.Round(MathF.Pow(goldenRatio,n) / MathF.Sqrt(5)));
    }
}