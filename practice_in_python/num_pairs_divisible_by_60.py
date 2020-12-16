# naive solution
# cnt = 0

# for i in range(len(time) - 1):
#     for j in range(i + 1, len(time)):
#         res = time[i] + time[j]
#         cnt = (cnt + 1) if res % 60 == 0 else cnt
# return cnt

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = 0
        m = {}
        for num in time:
            if -num % 60 in m:
                cnt += m[-num % 60]
            m[num % 60] = 1 if num % 60 not in m else m[num % 60] + 1

        return cnt