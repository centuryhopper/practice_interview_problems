from math import sqrt

class Solution:
    def fib(self, n: int) -> int:
        # used floats for better performance as high-precision isn't needed
        goldenRatio = (1+sqrt(5))/2;
        return round(pow(goldenRatio,n) / sqrt(5));
    