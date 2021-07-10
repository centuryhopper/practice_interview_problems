class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        cnt = 0
        for i in range(32):
            if cnt > 0 and n & (1 << i) == 1:
                # print(cnt,i)
                return False
            if n & (1 << i):
                cnt += 1
            # print(n & (1<<i), end=' ')
        return cnt == 1
