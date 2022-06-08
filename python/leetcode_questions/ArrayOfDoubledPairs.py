class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # use frequency hashmap tp check for dups of nonzero numbers. If any exist, then return false
        # otherwise check to see if the first half of the array, after it's sorted, has doubles
        d = collections.defaultdict(int)
        for num in arr:
            d[num]+=1
        # print(d)
        # handle zero cases
        # there must be an even number of zeros
        if 0 in d and d[0] % 2 == 1:
            print('zeros fucked u up')
            return False
        n = len(arr)
        # lst = []
        cnt = 0
        arr.sort()
        for num in arr:
            # if the current value's double exists and the current value hasn't been paired yet
            if d[2*num] != 0 and d[num] != 0:
                # lst.append((num,2*num))
                cnt+=1
                # decrement both
                d[2*num] = max(0,d[2*num]-1)
                d[num] = max(0,d[num]-1)
        # print(lst)
        # print(d)
        return cnt == n//2
        