class Solution:
    # brute force
    def reverseBits(self, n: int) -> int:
        s = '{:032b}'.format(n)[::-1]
        # print(s, len(s))
        return int('0b'+s,2)