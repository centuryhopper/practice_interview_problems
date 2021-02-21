class Solution:

    # cnt the number of arithemtic slices at a particular index
    # def dfs(self, a) -> int:
    #     if
    #     pass

    # arithmetic slice conditions: len(a) > 3 and at least one
    # instance where abs(a[i-1] - a[i]) == abs(a[i] - a[i+1])
    def numberOfArithmeticSlices(self, a: List[int]) -> int:
        if len(a) < 3:
            return 0
        retSum = 0

        i = 2
        # consistent difference
        diff = a[i-2] - a[i-1]
        print(len(a))
        # increase by 1 for each matching value after finding
        # a block of length 3, otherwise reset to 1
        rate = 1
        while i < len(a):

            # forms a block of three
            if diff == a[i-1] - a[i]:
                retSum += rate
                rate += 1
            else:
                rate = 1
                diff = a[i-1] - a[i]
            i += 1

        return retSum
