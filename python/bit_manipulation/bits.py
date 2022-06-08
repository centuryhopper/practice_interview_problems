
class Bits:
    def __init__(self):
        pass

    @staticmethod
    def countOnesAndZeros(x:int) -> (int, int):
        ones,zeros = 0,0
        while x > 0:
            ones += (x & 1)
            zeros += (~x & 1)
            x >>= 1
        return (ones, zeros)

    @staticmethod
    def rotateClockWise(x:int, n:int) -> int:
        BITS_IN_AN_INTEGER = 32
        # rotate x by n bits clockwise
        return (x >> n | x << (BITS_IN_AN_INTEGER - n))

if __name__ == '__main__':
    x = Bits.countOnesAndZeros(687)
    print(x)





