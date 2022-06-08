class Solution:
    def int_to_letter(self, num: int) -> str:
        if num > 26 or num <= 0:
            return None
        return chr(num + 97 - 1)

    def letter_to_int(self, letter: str) -> int:
        if len(letter) != 1:
            return None
        return ord(letter) - 97 + 1

    def getSmallestString(self, n: int, k: int) -> str:

        # string array ret val
        lst = [0] * n

        # goal: lst.count() must equal n at the end of the combo
        # the letters must add up to k

        for i in range(n-1, -1, -1):

            val = min(26, k - i)
            lst[i] = self.int_to_letter(val)
            k -= val


#         while n > 0:

#             if k - num < n - 1:
#                 num -= 1
#             else:
#                 lst.insert(0, self.int_to_letter(num))
#                 k -= num
#                 n -= 1

        # print(lst)

        return "".join(lst)
