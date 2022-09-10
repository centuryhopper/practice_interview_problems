
# derived from: https://github.com/mission-peace/interview/blob/master/src/com/interview/string/ZAlgorithm.java

from typing import List
import time

class ZAlgo:
    @staticmethod
    def calculateZ(s:str) -> List[int]:
        z = [0]*len(s)
        n = len(z)
        left = right = 0
        for k in range(1,n):
            if k > right:
                left = right = k
                while right < n and s[right] == s[right-left]:
                    right+=1
                z[k] = right - left
                # decrement here bc right ptr
                # is currently at the position where the comparison had a mismatch, so by doing so, we bring the right pointer back to the latest matching comparison
                right-=1
            else:
                k1 = k - left
                if z[k1] < right - k + 1:
                    z[k] = z[k1]
                else:
                    left = k
                    while right < len(s) and s[right] == s[right - left]:
                        right+=1
                    z[k] = right - left
                    right-=1
        return z

    @staticmethod
    def matchPattern(text: str, pattern: str) -> List[int]:
        newStr = f'{pattern}${text}'
        res = []
        z = ZAlgo.calculateZ(newStr)
        n = len(z)
        p = len(pattern)
        # get all values where they match the size of pattern
        for i in range(len(z)):
            if z[i] == p:
                res.append(i-p-1)
        return res

if __name__ == '__main__':
    text = "aaabcxyzaaaabczaaczabbaaaaaabc"
    pattern = "aaabc"
    start = time.perf_counter()
    res = ZAlgo.matchPattern(text,pattern)
    print(f'z algorithm time in ms: {(time.perf_counter() - start) * 1000}')
    print(res)

