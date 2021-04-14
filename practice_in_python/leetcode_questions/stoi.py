class Solution:

    # The function first discards as many whitespace characters
    # as necessary until the first non-whitespace character is found.
    # Then, starting from this character takes an optional initial plus
    # or minus sign followed by as many numerical digits as possible,
    # and interprets them as a numerical value.

    # / ==> float-friendly division     // ==> integer division
    def myAtoi(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0

        int_max = (2 ** 31) - 1
        int_min = -(2 ** 31)
        print(int_max / 10)

        i = 0
        ret = 0
        n = len(s)
        isNeg = False
        num_set = set('0123456789')

        # skip whitespaces
        while i < n and s[i] == ' ':
            i += 1

        if i < n and s[i] == '-':
            isNeg = True
            i += 1
        elif i < n and s[i] == '+':
            isNeg = False
            i += 1

        while i < n:

            if (not (s[i] in num_set) and ret > 0):
                return -ret if isNeg else ret
            elif not s[i] in num_set:
                return 0

            num = (ord(s[i]) - ord('0'))
            # check for integer overflow
            if (ret > int_max // 10) or (ret == int_max // 10 and num >= 8):
                return int_min if isNeg else int_max

            ret = ret * 10 + num

            print(ret)
            i += 1

        return -ret if isNeg else ret
